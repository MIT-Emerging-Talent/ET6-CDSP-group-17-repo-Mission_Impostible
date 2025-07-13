# ASOS_GraphReturns Data Preparation Report

## Overview
This report details the data preparation steps performed on the `ASOS_GraphReturns` dataset. The primary goal of this phase is to consolidate the disparate customer, product, and event data into a single, clean, and analysis-ready DataFrame. This involves merging tables, handling missing values, and ensuring appropriate data types for subsequent analysis and model building.

## Steps Performed

### 1. Data Loading
- The `customer_nodes_training.csv`, `event_table_training.csv`, and `product_nodes_training.csv` files were loaded into Pandas DataFrames. These files are located in `1_datasets/MIT Data Science/CSV Files/`.

### 2. Merging DataFrames
- The `event_table_training.csv` (which contains `hash(customerId)` and `hash(variantID)` along with `isReturned`) was used as the base for merging.
- It was merged with `customer_nodes_training.csv` using `hash(customerId)` as the key.
- The resulting DataFrame was then merged with `product_nodes_training.csv` using `hash(variantID)` as the key.
- All merges were performed using a `left` join to ensure that all records from the `event_table` were retained.

### 3. Column Renaming
- For clarity and ease of use, several hashed ID columns were renamed:
    - `hash(customerId)` to `customer_id`
    - `hash(variantID)` to `variant_id`
    - `hash(productID)` to `product_id`
    - `hash(supplierRef)` to `supplier_ref_id`

### 4. Handling Categorical Variables (One-Hot Encoding)
- During the exploration phase, it was noted that many categorical features were already one-hot encoded (e.g., `Country_A`, `productType_B`).
- However, original categorical columns like `shippingCountry`, `productType`, and `brandDesc` were still present.
- These remaining categorical columns were identified and one-hot encoded using `pd.get_dummies()` with `drop_first=True` to avoid multicollinearity.

### 5. Missing Value Check
- After merging, a check for missing values was performed. Any remaining missing values would need to be addressed (e.g., imputation or removal), but in this dataset, the merges were successful without introducing significant new missing data.

### 6. Data Type Verification
- The data types of all columns were re-verified to ensure they are appropriate for numerical computations and model training.

## Output
- The final prepared DataFrame, `merged_df`, contains all relevant information from the customer, product, and event tables, with appropriate column names and one-hot encoded categorical features.
- This prepared DataFrame has been saved as `prepared_asos_data.csv` in the `2_data_preparation/ASOS_GraphReturns/` directory for use in subsequent analysis and modeling phases.

## Summary of Prepared Data
- **Shape:** The final DataFrame has a shape of (number of events, number of features).
- **Columns:** Includes all original numerical features, renamed ID columns, and one-hot encoded versions of categorical features.
- **Target Variable:** The `isReturned` column remains as the target variable.

## Next Steps
With the data now prepared, the next phase will focus on:
1. **Data Exploration (Advanced):** Deeper statistical analysis and visualization of the prepared data to uncover relationships and patterns relevant to product returns.
2. **Feature Selection/Engineering:** Refining the feature set for model training.
3. **Model Building:** Developing and evaluating predictive models.
4. **Reporting:** Documenting all steps and findings.