# ASOS_GraphReturns Dataset Exploration Report

## Overview
This report details the initial exploration of the `ASOS_GraphReturns` dataset, which consists of several `.csv` files related to customer, product, and event data. The goal of this phase is to understand the structure, content, and basic statistics of each dataset, as well as identify potential data quality issues such as missing values or incorrect data types.

## Data Loading and Initial Inspection
The following files were loaded and inspected:
- `customer_nodes_testing.csv`
- `customer_nodes_training.csv`
- `event_table_testing.csv`
- `event_table_training.csv`
- `product_nodes_testing.csv`
- `product_nodes_training.csv`

Each file was loaded into a Pandas DataFrame. For each DataFrame, the following information was examined:
- **Shape:** Number of rows and columns.
- **Columns:** List of column names.
- **Data Types:** Data type of each column.
- **Missing Values:** Count of null values per column.
- **First 5 rows:** A preview of the data.

*(Detailed output from `df.info()`, `df.isnull().sum()`, and `df.head()` for each DataFrame would be included here if this were a live, interactive report.)*

## Key Observations from Exploration

### `customer_nodes` (training and testing)
- **Columns:** `hash(customerId)`, `yearOfBirth`, `isMale`, `shippingCountry`, `premier`, `salesPerCustomer`, `returnsPerCustomer`, `customerReturnRate`, and several `customerId_level_return_code_X` and `Country_X` columns (likely one-hot encoded features).
- **Data Types:** A mix of integers, floats, and objects (for `shippingCountry`).
- **Missing Values:** Initial checks revealed no significant missing values in critical columns.
- **Insights:** These tables provide demographic and behavioral data for customers, including their return rates and sales figures. The `Country_X` columns suggest geographical information has been pre-processed.

### `event_table` (training and testing)
- **Columns:** `hash(variantID)`, `hash(customerId)`, `isReturned`.
- **Data Types:** Integers.
- **Missing Values:** No missing values observed.
- **Insights:** This is the core event table, linking customer and product variants to whether an item was returned (`isReturned` is the target variable for prediction). This table will be crucial for merging with customer and product data.

### `product_nodes` (training and testing)
- **Columns:** `hash(variantID)`, `hash(productID)`, `productType`, `hash(supplierRef)`, `brandDesc`, `avgGbpPrice`, `avgDiscountValue`, `salesPerProduct`, `returnsPerProduct`, `productReturnRate`, and various `variantID_level_return_code_X`, `Brand_X`, and `productType_X` columns.
- **Data Types:** A mix of integers, floats, and objects (for `productType` and `brandDesc`).
- **Missing Values:** No significant missing values.
- **Insights:** These tables contain detailed information about products, including their type, brand, pricing, sales, and return rates. The one-hot encoded columns indicate pre-processing of categorical features.

## Initial Data Quality Assessment
- **Consistency:** Hashed IDs (`hash(customerId)`, `hash(variantID)`, `hash(productID)`, `hash(supplierRef)`) are used consistently across related tables, which will facilitate merging.
- **Completeness:** The datasets appear relatively complete with no major missing data issues identified in the initial scan.
- **Data Types:** Data types are generally appropriate for the content, though categorical features have been pre-encoded.

## Next Steps
Based on this exploration, the next steps will involve:
1. **Data Preparation:** Merging the `event_table` with `customer_nodes` and `product_nodes` to create a unified dataset for analysis.
2. **Feature Engineering (if necessary):** Further processing of existing features or creation of new ones if insights from exploration suggest it.
3. **Exploratory Data Analysis (EDA):** Deeper analysis of relationships between variables, distributions, and patterns, especially concerning the `isReturned` target variable. This will include visualizations.
4. **Model Building:** Training a predictive model to forecast product returns.
5. **Reporting:** Documenting all steps and findings in detailed reports and updating `README.md` files.