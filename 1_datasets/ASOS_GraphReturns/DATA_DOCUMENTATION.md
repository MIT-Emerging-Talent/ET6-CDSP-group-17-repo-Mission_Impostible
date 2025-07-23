# ASOS GraphReturns Dataset Documentation

This document provides comprehensive documentation for the ASOS GraphReturns Dataset, including its origin, structure, features, known issues, and the steps taken in this project for data processing and preparation for predictive modeling.

## ASOS Graph Returns Dataset Overview

This repository contains code and documentation related to the ASOS GraphReturns Dataset, used for predicting product returns in an e-commerce context. The dataset's graph structure allows for advanced analysis using graph-based machine learning techniques.

## Project Overview

This project uses the ASOS GraphReturns dataset to predict whether a customer will return a purchased item. We model this problem using Graph Neural Networks (GNNs), which are well-suited to the relational structure of the data—customers, products, and transactions form a natural graph.

## Dataset Information

*   **Source:** Collected by ASOS, a leading online fashion retailer. Released via OSF under CC-BY 4.0 license and used in McGowan et al. (2023) and Springer 2023.

*   **Structure:** The dataset is structured as a graph with two types of nodes and one type of edge:

##  Structure

The dataset is structured as a graph:

    *   **Nodes:**
        *   **Customer Nodes:** Representing individual customers with anonymized demographic information. As seen in the notebook, attributes include a hashed customer ID (`hash(customerId)`), `yearOfBirth`, `isMale`, `shippingCountry`, `premier` status, and aggregated behavioral metrics like `salesPerCustomer`, `returnsPerCustomer`, and `customerReturnRate`. It also includes one-hot encoded features for country and customer-level return codes derived from the data.
        *   **Product Nodes:** Representing product variants. As seen in the notebook, attributes include hashed variant ID (`hash(variantID)`), hashed product ID (`hash(productID)`), `productType`, hashed supplier reference (`hash(supplierRef)`), `brandDesc`, price information (`avgGbpPrice`, `avgDiscountValue`), and aggregated performance metrics like `salesPerProduct`, `returnsPerProduct`, and `productReturnRate`. It also includes one-hot encoded features for product type, brand, and variant-level return codes derived from the data.

    *   **Edges:**
        *   **Transaction Edges:** Representing individual purchase events, linking customer nodes to product nodes. The key attribute used in this project is `isReturned` (1 = returned, 0 = kept), which is the target variable for prediction. Based on the provided general documentation, these edges also contain `timestamp` and `size` information, although these were not explicitly used in the provided notebook code.

##  Schema:
  
| Node Type | Attributes |
|-----------|------------|
| Customer  | customer_id, age_group, region |
| Product   | product_id, category, brand, price |
| Edge      | transaction_id, timestamp, size, return_flag |
   
    *   **Node Type:** Customer
        *   **Attributes:** `customer_id`, `age_group`, `region` (as per general documentation, though specific columns in the provided data differ)
    *   **Node Type:** Product
        *   **Attributes:** `product_id`, `category`, `brand`, `price` (as per general documentation, though specific columns in the provided data differ)
    *   **Edge Type:** Transaction
        *   **Attributes:** `transaction_id`, `timestamp`, `size`, `return_flag` (as per general documentation)

## Dataset Features

*   **Graph-based Structure:** The inherent graph structure enables potential application of graph-based machine learning techniques, allowing for message passing and learning representations that capture complex relationships between customers, products, and transactions.
*   **Supports Edge Classification:** The dataset is well-suited for edge classification tasks, specifically predicting the `isReturned` attribute of a transaction edge.
*   **Includes Temporal and Categorical Features:** The dataset contains a temporal feature (`yearOfBirth`) and numerous categorical features (e.g., `shippingCountry`, `productType`, `brandDesc`, `premier`, and various level-specific return codes and one-hot encoded Country, Brand, and ProductType features).

## Known Issues

*   **Anonymized Identifiers:** Customer, variant, product, and supplier IDs are hashed (`hash(...)`), meaning the original identifiers are not available. This prevents direct linkage to external data sources or detailed analysis requiring original, identifiable IDs.
*   **Imbalanced Data:** The provided information notes that some product categories dominate return behavior, suggesting potential class imbalance issues for certain types of analysis or modeling approaches. The notebook output shows that the `isReturned` target variable is also imbalanced (464,466 returned vs 383,988 not returned in the training data).
*   **Missing Values:** The original dataset is noted to have some transactions lacking full metadata. While not explicitly handled in the provided notebook's processing steps, this is a potential data quality concern for more complex analyses.
*   **Duplicate Columns:** As observed in the notebook, there are duplicate columns present in both `customer_nodes` (`customerId_level_return_code_D` appears twice) and `product_nodes` (`variantID_level_return_code_D` appears twice). This is a data quality issue in the source files that needs to be considered during data processing.
*   **Feature Redundancy:** The dataset includes both raw counts and calculated rates (e.g., `salesPerCustomer` and `customerReturnRate`), as well as various one-hot encoded features and level-specific return codes, which might introduce feature redundancy or multicollinearity.

## Data Processing Steps (as per the Notebook)

To recreate the merged dataset used for modeling in the notebook, the following key steps were performed using pandas:

1.  **Load Data:** The training data from the pickle files (`customer_nodes_training.p`, `event_table_training.p`, `product_nodes_training.p`) were loaded into pandas DataFrames.
2.  **Convert to CSV:** The loaded DataFrames were saved as CSV files in a directory named `csv_outputs`. This step is useful for easier inspection and potential use with other tools.
3.  **Merge DataFrames:** The `event_table` DataFrame was merged with `customer_nodes` on `hash(customerId)` and then with `product_nodes` on `hash(variantID)` to create a single merged DataFrame (`merged_df`).
4.  **Rename Columns:** Some columns were renamed for clarity (e.g., `hash(customerId)` to `customer_id`, `hash(variantID)` to `variant_id`).
5.  **Feature Selection:** Columns identified as identifiers or non-numeric (excluding the target) were dropped for the feature set (`X`).
6.  **One-Hot Encoding:** Categorical features in the `X` DataFrame were converted into numerical format using one-hot encoding (`pd.get_dummies`). The `drop_first=True` argument was used to avoid multicollinearity.
7.  **Target Variable:** The `isReturned` column was separated as the target variable (`y`).
8.  **Train-Test Split:** The feature set `X` and target variable `y` were split into training and testing sets (`X_train`, `X_test`, `y_train`, `y_test`) using `train_test_split` from `sklearn.model_selection` with a test size of 20% and a `random_state` for reproducibility.

##  Source
- Collected by ASOS, a leading online fashion retailer.
- Released via [OSF](https://osf.io/c793h/) under CC-BY 4.0 license.
- Used in [McGowan et al. (2023)](https://arxiv.org/abs/2302.14096) and [Springer 2023](https://link.springer.com/chapter/10.1007/978-3-031-22192-7_6).
