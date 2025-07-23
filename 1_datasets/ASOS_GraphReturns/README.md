
# ASOS Graph Returns Dataset

This repository contains code and documentation related to the ASOS GraphReturns Dataset, used for predicting product returns in an e-commerce context. The dataset's graph structure allows for advanced analysis using graph-based machine learning techniques.

##  Project Overview

This project uses the [ASOS GraphReturns dataset](https://drive.google.com/drive/folders/1xpCMMrpNtFms7KKrCIVClTbYNZQUcSpg?usp=sharing) to predict whether a customer will return a purchased item. We model this problem using **Graph Neural Networks (GNNs)**, which are well-suited to the relational structure of the data—customers, products, and transactions form a natural graph.

## Dataset Information

*   **Source:** Collected by ASOS, a leading online fashion retailer. Released via OSF under CC-BY 4.0 license and used in McGowan et al. (2023) and Springer 2023.
*   **Structure:** The dataset is structured as a graph with two types of nodes and one type of edge:
    *   **Nodes:**
        *   **Customer:** Representing individual customers with anonymized demographic information (e.g., ID, age group, region).
        *   **Product:** Representing product variants with attributes like ID, category, brand, and price.
    *   **Edges:**
        *   **Transaction:** Connecting customers and products, representing a purchase event with a timestamp, size information, and a flag indicating whether the product was returned (`return_flag`: 1 = returned, 0 = kept).
*   **Example Schema:**
    *   **Node Type:** Customer
        *   **Attributes:** `customer_id`, `age_group`, `region`
    *   **Node Type:** Product
        *   **Attributes:** `product_id`, `category`, `brand`, `price`
    *   **Edge Type:** Transaction
        *   **Attributes:** `transaction_id`, `timestamp`, `size`, `return_flag`
*   **Features:**
    *   Graph-based structure enables message passing and representation learning.
    *   Supports edge classification (predicting returns).
    *   Includes temporal and categorical features.
*   **Known Issues:**
    *   **Anonymized:** No direct customer identifiers are available.
    *   **Imbalanced:** Some product categories dominate return behavior.
    *   **Missing values:** Some transactions lack full metadata.

## Project Goal: Predicting Product Returns

The primary objective of this project is to develop a model that predicts whether a product purchased by a customer will be returned, utilizing the information available in the ASOS GraphReturns dataset.

## Potential Flaws and Limitations of the Approach

*   **Data Quality:** The presence of duplicate columns in the original data (e.g., `customerId_level_return_code_D`, `variantID_level_return_code_D`) required careful handling during processing.
*   **Anonymization:** Hashed identifiers prevent linking to external data sources or detailed analysis requiring original IDs.
*   **Static Model:** The current model is trained on a static dataset and may not adapt well to evolving trends in customer behavior or product characteristics without retraining.
*   **Limited Feature Set:** While a range of features were used, exploring additional features or more sophisticated feature engineering techniques could potentially improve model performance.
*   **Model Interpretability:** While feature importances provide some insight, the Random Forest model itself can be a "black box," making it challenging to fully explain individual predictions.

## Files in this Repository

*   `README.md`: This file provides an overview of the dataset and project.
*   `Documentation.md`: Detailed documentation on the dataset's structure, origin, and known issues.
*   `ASOS.ipynb`: Python script containing the data loading, cleaning, merging, and splitting logic.


## How to Recreate the Analysis

1.  Obtain the ASOS GraphReturns dataset files (`.p` files).
2.  Place the data files in the appropriate directory (or modify the `ASOS.ipynb` script to point to their location).
3.  Run the `ASOS.ipynb` script to load, process, and split the data.
4.  Use the processed data (`X_train`, `X_test`, `y_train`, `y_test`) to train and evaluate the model.

### Structure
- **event_table_training.p / event_table_testing.p**: Purchase events.
- **customer_nodes_training.p / customer_nodes_testing.p**: Customer attributes.
- **product_nodes_training.p / product_nodes_testing.p**: Product-level features.

### Key Columns
- `hash(customerId)`, `hash(variantID)`, `isReturned`
- Demographics: `yearOfBirth`, `isMale`, `shippingCountry`, `premier`
- Product attributes: `productTypeID`, `brandID`, `price`, `returnRate`

### Known Flaws
- Includes only returners → selection bias
- No timestamps for temporal analysis
- Hashed IDs limit interpretability
- Possible class imbalance

### 🔗 Resources
- Dataset: [OSF Repository](https://osf.io/c793h/)


