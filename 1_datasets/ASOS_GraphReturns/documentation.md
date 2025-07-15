# Data Documentation

This document describes the dataset used for predicting product returns, including its origin, structure, potential flaws, and steps for recreation.

## Dataset Origin

The dataset was provided in several pickle (.p) files, which were loaded into pandas DataFrames for analysis and modeling. The specific origin of the data (e.g., company source, collection method) is not detailed in the provided files themselves.

## Dataset Structure

The dataset is composed of three main files, which were merged based on common IDs:

1.  **`customer_nodes_training.p` / `customer_nodes_testing.p`**: These files contain information about individual customers.
    *   **Key Columns:** `hash(customerId)` (unique identifier for customers), `yearOfBirth`, `isMale`, `shippingCountry`, `premier` (likely a loyalty status), `salesPerCustomer`, `returnsPerCustomer`, `customerReturnRate`, and various `customerId_level_return_code_*` and `Country_*` one-hot encoded features.

2.  **`product_nodes_training.p` / `product_nodes_testing.p`**: These files contain information about individual product variants.
    *   **Key Columns:** `hash(variantID)` (unique identifier for product variants), `hash(productID)` (identifier for the base product), `productType`, `hash(supplierRef)`, `brandDesc`, `avgGbpPrice`, `avgDiscountValue`, `salesPerProduct`, `returnsPerProduct`, `productReturnRate`, and various `variantID_level_return_code_*`, `Brand_*`, and `productType_*` one-hot encoded features.

3.  **`event_table_training.p` / `event_table_testing.p`**: This file serves as the core transaction or event log, linking customers and products and containing the target variable.
    *   **Key Columns:** `hash(variantID)`, `hash(customerId)`, and `isReturned` (the target variable, indicating whether the product variant in this event was returned).

The training and testing datasets are provided separately.

## Potential Data Flaws

Several potential issues were observed in the dataset:

*   **Hashed Identifiers:** Customer, variant, product, and supplier IDs are hashed (`hash(...)`), meaning the original identifiers are not available. This prevents linking the data back to specific real-world entities or external datasets using these IDs.
*   **Duplicate Columns:** There are duplicate columns present in both `customer_nodes` (`customerId_level_return_code_D` appears twice) and `product_nodes` (`variantID_level_return_code_D` appears twice). This indicates a data quality issue that should ideally be addressed before modeling, although the current approach handles this by dropping one of the duplicates implicitly during one-hot encoding.
*   **Potential Biases:** The dataset reflects past transactions and customer behavior. It may contain biases related to specific time periods, promotional activities, or demographic distributions that might affect the generalizability of a model trained on this data to future events.
*   **Feature Redundancy/Multicollinearity:** The presence of both raw counts (`salesPerCustomer`, `returnsPerCustomer`, `salesPerProduct`, `returnsPerProduct`) and derived rates (`customerReturnRate`, `productReturnRate`) along with various one-hot encoded categorical features and level-specific return codes suggests potential redundancy and multicollinearity among features.

## Dataset Recreation Steps

To recreate the merged dataset used for modeling from the provided pickle files, follow these steps:

1.  **Load the pickle files:** Use the `pickle` library in Python to load the `.p` files into pandas Dataframes.
    ```python
    import pickle
    import pandas as pd

    file_names = [
        "customer_nodes_training.p",
        "event_table_training.p",
        "product_nodes_training.p"
    ]

    loaded_data = {}
    for name in file_names:
        with open(name, "rb") as f:
            loaded_data[name] = pickle.load(f)

    event_table = loaded_data["event_table_training.p"]
    customer_nodes = loaded_data["customer_nodes_training.p"]
    product_nodes = loaded_data["product_nodes_training.p"]
    ```
2.  **Merge the DataFrames:** Merge the `event_table`, `customer_nodes`, and `product_nodes` DataFrames using the shared hashed IDs.
    ```python
    merged_df = event_table.merge(customer_nodes, on='hash(customerId)') \\
                           .merge(product_nodes, on='hash(variantID)')
    ```
3.  **Rename Columns (Optional but Recommended):** Rename the hashed ID columns for clarity.
    ```python
    merged_df.rename(columns={
        'hash(customerId)': 'customer_id',
        'hash(variantID)': 'variant_id'
    }, inplace=True)
    ```
4.  **Prepare Data for Modeling:** Separate features (X) and the target variable (y). Handle categorical variables (e.g., using one-hot encoding). Drop unnecessary ID columns.
    ```python
    # Drop non-numeric or ID columns and the target variable
    X = merged_df.drop(columns=['isReturned', 'hash(customerId)', 'hash(variantID)', 'hash(productID)', 'hash(supplierRef)'], errors='ignore')

    # One-hot encode categorical variables (handling potential duplicates)
    X = pd.get_dummies(X, drop_first=True)

    # Define the target variable
    y = merged_df['isReturned']
    ```
5.  **Split Data:** Split the data into training and testing sets for model development and evaluation.
    ```python
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    ```

These steps reproduce the primary DataFrame used for the machine learning model training and evaluation as shown in the notebook.
"""
