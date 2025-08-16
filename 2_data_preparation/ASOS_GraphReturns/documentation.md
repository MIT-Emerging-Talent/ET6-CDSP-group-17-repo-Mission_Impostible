# 🛠️ Technical Documentation: Product Return Data Preparation

---

## 1. Data Description

Three primary datasets were used:

| File Name                     | Description                          | Shape             |
|------------------------------|--------------------------------------|-------------------|
| `customer_nodes_training.csv`| Customer features                    | (777,001 × 30)    |
| `product_nodes_training.csv` | Product (variant) features           | (411,495 × 44)    |
| `event_table_training.csv`   | Customer-product interactions        | (1,369,133 × 3)   |

- **Key Identifiers**:
  - Customer ID: `hash(customerid)` → standardized to `customer_id`
  - Product ID: `hash(variantid)` → standardized to `product_id`
- **Target Variable**: `isreturned` (binary classification)

---

## 2. Data Preprocessing

### 🔤 Column Name Cleaning
- Applied `clean_col_names` to all DataFrames:
  - Stripped whitespace
  - Converted to lowercase
  - Replaced spaces with underscores

### 🎯 Label Identification
- Target variable: `isreturned`
- Label distribution:
  - Returns (1): 757,227 (55.3%)
  - Non-returns (0): 611,906 (44.7%)

### 🔗 Data Merging
- `df_events` left-merged with `df_customers` on `hash(customerid)` ↔ `customer_id`
- Result merged with `df_products` on `hash(variantid)` ↔ `product_id`
- Final merged DataFrame shape: **(1,369,133 × 77)**

### 🧼 Missing Value Handling
- Dropped columns with >80% missing values (none dropped)
- Imputation strategies:
  - **Numerical**: Median (`SimpleImputer`)
  - **Categorical**: Constant `'missing'` (`SimpleImputer`)

### 🧬 Feature Type Identification
- Identified 73 numeric features and 3 categorical features
- Excluded ID columns used for merging

### ⚙️ Preprocessing Pipelines
- **Numerical Pipeline**:
  - `SimpleImputer(strategy='median')`
  - `StandardScaler()`
- **Categorical Pipeline**:
  - `SimpleImputer(strategy='constant', fill_value='missing')`
  - `OneHotEncoder(handle_unknown='ignore', sparse_output=False)`
- Combined using `ColumnTransformer`
- Transformed feature matrix shape: **(1,369,133 × 107)**
- Saved preprocessor as: `preprocessor_train.joblib`

---

## 3. Train/Validation Split

- Used `train_test_split` with:
  - `test_size=0.1`
  - `stratify=y`
  - `random_state=42`
- Shapes:
  - `X_train`: (1,232,219 × 107)
  - `X_val`: (136,914 × 107)
  - `y_train`: (1,232,219,)
  - `y_val`: (136,914,)
- Saved as: `tabular_train_val.joblib`

---

## 4. Bipartite Graph Creation

Constructed using `networkx` to model customer-product interactions:

### 🧩 Nodes
- **Customers**: From `df_customers`, labeled `bipartite=0`
- **Products**: From `df_products`, labeled `bipartite=1`
- Node attributes: All non-ID, non-NA features

### 🔗 Edges
- Created from `df_events`
- Each edge connects a customer to a product
- Edge attribute: `label` = `isreturned`

### 📊 Graph Stats
- Nodes: **487,508**
- Edges: **50,275**
- Saved merged graph data as: `merged_events_train.joblib`

---

## 5. Technical Visualizations (Suggested)

To enhance interpretability and validate preprocessing in the next step, we can do the following:

### 🔥 Missingness Heatmap
- Visualize missing data patterns in the merged DataFrame before column drops

### 📈 Feature Distributions
- **Numerical**: Histograms/density plots before and after scaling
  - Examples: `yearofbirth`, `salespercustomer`, `avggbpprice`
- **Categorical**: Bar plots showing category counts and imputation effects
  - Example: `shippingcountry`

### 🔗 Correlation Matrix
- Heatmap of pairwise correlations among numerical features post-imputation

### 🕸️ Bipartite Graph Properties
- Degree distribution plots:
  - Customer nodes: Number of products interacted with
  - Product nodes: Number of customers interacted with
- Subgraph visualization:
  - Small sample of nodes and edges to illustrate structure
