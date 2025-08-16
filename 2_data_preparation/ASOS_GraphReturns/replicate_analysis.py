# replicate_analysis.py

import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import joblib
import networkx as nx

print("Starting analysis replication script...")

# -------- 1) Paths --------
# Assuming data is in a 'data' subdirectory relative to the script execution location
# You might need to adjust this path depending on where you place the data files
DATA_DIR = Path("./data")
files = {
    "customer_train": DATA_DIR / "customer_nodes_training.csv",
    "product_train":  DATA_DIR / "product_nodes_training.csv",
    "events_train":   DATA_DIR / "event_table_training.csv",
    "customer_test":  DATA_DIR / "customer_nodes_testing.csv",
    "product_test":   DATA_DIR / "product_nodes_testing.csv",
    "events_test":    DATA_DIR / "event_table_testing.csv",
}

print(f"Expecting data in directory: {DATA_DIR.resolve()}")

# -------- 2) Load CSVs --------
print("Loading datasets...")
try:
    # Added low_memory=False to potentially help with mixed types/parsing issues
    df_customers = pd.read_csv(files["customer_train"], low_memory=False)
    df_products  = pd.read_csv(files["product_train"], low_memory=False)
    df_events    = pd.read_csv(files["events_train"], low_memory=False)
    print("Datasets loaded successfully.")
    print("Shapes (customers, products, events):", df_customers.shape, df_products.shape, df_events.shape)
except FileNotFoundError as e:
    print(f"Error loading data files: {e}")
    print(f"Please ensure the data files are located in the '{DATA_DIR.resolve()}' directory.")
    exit() # Exit the script if data files are not found
except pd.errors.ParserError as e:
    print(f"Error parsing data files: {e}")
    print(f"Please check the data files for formatting issues, especially around the line mentioned in the error.")
    exit() # Exit the script if parsing fails


# -------- 3) Clean column names --------
print("Cleaning column names...")
def clean_col_names(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

df_customers = clean_col_names(df_customers)
df_products = clean_col_names(df_products)
df_events = clean_col_names(df_events)
print("Column names cleaned.")

# -------- 4) Identify label column --------
print("Identifying label column...")
label_col = None
if 'isreturned' in df_events.columns:
    label_col = 'isreturned'
else:
    possible_label_names = ["return", "is_return", "label", "returned"]
    for col in df_events.columns:
        if col.strip().lower() in possible_label_names:
            label_col = col
            break

if label_col is None:
    print("Error: No label column found; check event table column names.")
    exit()

print(f"Label column: {label_col}")
print("Label distribution (train):")
print(df_events[label_col].value_counts(normalize=False))
print(df_events[label_col].value_counts(normalize=True))

# -------- 5) Suggest ID columns --------
print("Identifying ID columns...")
def suggest_id_columns(df, label):
    cols = df.columns.tolist()
    cust_candidates = [c for c in cols if any(k in c.lower() for k in ["cust", "customer"])]
    prod_candidates = [c for c in cols if any(k in c.lower() for k in ["prod", "product", "variant"])]
    return cust_candidates, prod_candidates

cust_event_candidates, prod_event_candidates = suggest_id_columns(df_events, "Events")
cust_node_candidates, _ = suggest_id_columns(df_customers, "Customers")
_, prod_node_candidates = suggest_id_columns(df_products, "Products")

cust_id_col_event = cust_event_candidates[0] if cust_event_candidates else None
prod_id_col_event = prod_event_candidates[0] if prod_event_candidates else None
cust_id_col_node = cust_node_candidates[0] if cust_node_candidates else None
prod_id_col_node = prod_node_candidates[0] if prod_node_candidates else None

if not all([cust_id_col_event, prod_id_col_event, cust_id_col_node, prod_id_col_node]):
    print("Error: Could not identify customer or product ID columns for merging.")
    exit()

print(f"Identified customer ID (event): {cust_id_col_event}")
print(f"Identified product ID (event): {prod_id_col_event}")
print(f"Identified customer ID (node): {cust_id_col_node}")
print(f"Identified product ID (node): {prod_id_col_node}")


# -------- 6) Standardize ID column names --------
print("Standardizing ID column names...")
if cust_id_col_node != "customer_id":
    df_customers = df_customers.rename(columns={cust_id_col_node: "customer_id"})
    cust_id_col_node = "customer_id"

if prod_id_col_node != "product_id":
    df_products = df_products.rename(columns={prod_id_col_node: "product_id"})
    prod_id_col_node = "product_id"
print("ID column names standardized.")


# -------- 7) Merge datasets --------
print("Merging datasets...")
df = df_events.merge(df_customers, left_on=cust_id_col_event, right_on=cust_id_col_node, how="left", suffixes=("", "_cust"))
df = df.merge(df_products, left_on=prod_id_col_event, right_on=prod_id_col_node, how="left", suffixes=("", "_prod"))

print("Datasets merged.")
print("Merged dataset shape:", df.shape)

# -------- 8) Missingness report --------
print("Handling missing values...")
def missing_report(df_in):
    miss = df_in.isna().mean().sort_values(ascending=False)
    return miss[miss > 0]

high_missing_thresh = 0.80
missing_cols = missing_report(df)
cols_to_drop = missing_cols[missing_cols > high_missing_thresh].index.tolist()
print(f"Dropping {len(cols_to_drop)} cols with >{high_missing_thresh*100}% missing:", cols_to_drop)
df = df.drop(columns=cols_to_drop)
print("High missingness columns dropped.")

# -------- 9) Feature types --------
print("Identifying feature types...")
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
if label_col in numeric_cols:
    numeric_cols.remove(label_col)

categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
ids_to_remove_from_cat = [cust_id_col_event, prod_id_col_event, 'customer_id', 'product_id']
categorical_cols = [c for c in categorical_cols if c not in ids_to_remove_from_cat]

print("Numeric features identified:", len(numeric_cols))
print("Categorical features identified:", len(categorical_cols))

# -------- 10) Preprocessing pipelines --------
print("Defining preprocessing pipelines...")
num_pipeline = Pipeline([
    ("impute", SimpleImputer(strategy="median")),
    ("scale", StandardScaler())
])

cat_pipeline = Pipeline([
    ("impute", SimpleImputer(strategy="constant", fill_value="missing")),
    ("ohe", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
])

preprocessor = ColumnTransformer([
    ("num", num_pipeline, numeric_cols),
    ("cat", cat_pipeline, categorical_cols)
], remainder="drop", sparse_threshold=0)

X = df.drop(columns=[label_col])
y = df[label_col].astype(int)

print("Fitting preprocessor...")
preprocessor.fit(X)
X_trans = preprocessor.transform(X)
print("Preprocessing complete.")
print("Transformed X shape:", X_trans.shape)

print("Saving preprocessor...")
joblib.dump(preprocessor, "preprocessor_train.joblib")
print("Preprocessor saved as preprocessor_train.joblib")

# -------- 11) Train/validation split --------
print("Performing train/validation split...")
X_train, X_val, y_train, y_val = train_test_split(X_trans, y, test_size=0.1, stratify=y, random_state=42)
print("Train/val sizes:", X_train.shape, X_val.shape, y_train.shape, y_val.shape)

print("Saving train/validation sets...")
joblib.dump((X_train, X_val, y_train, y_val), "tabular_train_val.joblib")
print("Train/validation sets saved as tabular_train_val.joblib")

# -------- 12) Build bipartite graph --------
print("Building bipartite graph...")
G = nx.Graph()

# Only add nodes for customers and products that exist in the merged df
# This ensures consistency between tabular data and graph nodes
unique_customers_in_merged = df['customer_id'].dropna().unique()
unique_products_in_merged = df['product_id'].dropna().unique()

cust_feat_cols = [c for c in df_customers.columns if c != "customer_id"]
# Filter customer nodes to only include those in the merged data
df_customers_filtered = df_customers[df_customers['customer_id'].isin(unique_customers_in_merged)].copy()
for _, row in df_customers_filtered.iterrows():
    node_id = f"c_{row['customer_id']}"
    # Add node features, handling potential NaN values in features
    node_features = {k: row[k] for k in cust_feat_cols if pd.notna(row[k])}
    G.add_node(node_id, bipartite=0, **node_features)


prod_feat_cols = [c for c in df_products.columns if c != "product_id"]
# Filter product nodes to only include those in the merged data
df_products_filtered = df_products[df_products['product_id'].isin(unique_products_in_merged)].copy()
for _, row in df_products_filtered.iterrows():
    node_id = f"p_{row['product_id']}"
    # Add node features, handling potential NaN values in features
    node_features = {k: row[k] for k in prod_feat_cols if pd.notna(row[k])}
    G.add_node(node_id, bipartite=1, **node_features)

# Add edges based on events in the merged dataframe
# This ensures edges connect nodes that are actually present in the graph
df_events_for_graph = df[['hash(customerid)', 'hash(variantid)', label_col]].copy()
# Rename columns to match the node IDs we will create
df_events_for_graph = df_events_for_graph.rename(columns={'hash(customerid)': 'customer_id_event', 'hash(variantid)': 'product_id_event'})


for _, r in df_events_for_graph.iterrows():
    c_id_event = r['customer_id_event']
    p_id_event = r['product_id_event']
    label = int(r[label_col])

    c_node_id = f"c_{c_id_event}"
    p_node_id = f"p_{p_id_event}"

    # Only add edge if both nodes exist in the graph
    if G.has_node(c_node_id) and G.has_node(p_node_id):
        # Check if edge already exists to avoid duplicates if events table has duplicates
        if not G.has_edge(c_node_id, p_node_id):
             G.add_edge(c_node_id, p_node_id, label=label)
        else:
            # Handle duplicate edges if necessary, e.g., aggregate labels or add as attribute list
            # For now, we'll just ensure it's added once with the last seen label
            pass


print("Bipartite graph built.")
print("Graph nodes/edges:", G.number_of_nodes(), G.number_of_edges())

# -------- 13) Save processed datasets (optional, already saved tabular data) --------
# Saving the merged dataframe after initial cleaning and dropping high missingness columns
print("Saving merged dataframe after initial processing...")
joblib.dump(df, "merged_events_train.joblib")
print("Merged dataframe saved as merged_events_train.joblib")

print("Analysis replication script finished.")