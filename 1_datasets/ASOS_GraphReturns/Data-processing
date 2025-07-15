
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_names):
    \"\"\"Loads data from pickle files.\"\"\"
    loaded_data = {}
    for name in file_names:
        with open(name, "rb") as f:
            loaded_data[name] = pickle.load(f)
    return loaded_data

def process_and_split_data(loaded_data):
    \"\"\"Merges data, cleans, and splits for modeling.\"\"\"
    event_table = loaded_data["event_table_training.p"]
    customer_nodes = loaded_data["customer_nodes_training.p"]
    product_nodes = loaded_data["product_nodes_training.p"]

    # Merge the dataframes
    merged_df = event_table.merge(customer_nodes, on='hash(customerId)') \\
                           .merge(product_nodes, on='hash(variantID)')

    # Rename columns
    merged_df.rename(columns={
        'hash(customerId)': 'customer_id',
        'hash(variantID)': 'variant_id'
    }, inplace=True)

    # Prepare data for modeling
    # Drop non-numeric or ID columns and the target variable
    # Use errors='ignore' to handle potential duplicate columns like 'customerId_level_return_code_D'
    X = merged_df.drop(columns=['isReturned', 'hash(customerId)', 'hash(variantID)', 'hash(productID)', 'hash(supplierRef)'], errors='ignore')

    # One-hot encode categorical variables
    X = pd.get_dummies(X, drop_first=True)

    # Define the target variable
    y = merged_df['isReturned']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    # List of training file names
    training_files = [
        "customer_nodes_training.p",
        "event_table_training.p",
        "product_nodes_training.p"
    ]

    # Load data
    loaded_training_data = load_data(training_files)

    # Process and split data
    X_train, X_test, y_train, y_test = process_and_split_data(loaded_training_data)

    print("Data processing complete.")
    print(f"X_train shape: {X_train.shape}")
    print(f"X_test shape: {X_test.shape}")
    print(f"y_train shape: {y_train.shape}")
    print(f"y_test shape: {y_test.shape}")

