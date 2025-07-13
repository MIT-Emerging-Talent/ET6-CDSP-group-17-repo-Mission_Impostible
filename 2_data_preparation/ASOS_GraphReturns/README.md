# ASOS_GraphReturns Data Preparation

This directory contains files related to the data preparation phase for the `ASOS_GraphReturns` dataset.

## Data Preparation Phase

The data preparation phase involved transforming the raw data into a clean, merged, and analysis-ready format. Key steps included:

- **Data Loading:** Loading the customer, event, and product training datasets.
- **Data Merging:** Combining the three datasets (`customer_nodes`, `event_table`, and `product_nodes`) into a single comprehensive DataFrame using `customer_id` and `variant_id` as keys.
- **Column Renaming:** Renaming hashed ID columns for better readability and usability.
- **Categorical Variable Handling:** Applying one-hot encoding to remaining categorical features (`shippingCountry`, `productType`, `brandDesc`) that were not pre-encoded.
- **Missing Value Check:** Verifying the absence of significant missing values after merging and transformations.

For a detailed report of the data preparation steps and outcomes, please refer to `report.md` in this directory.

## Files:
- `prepare_asos.ipynb`: Jupyter Notebook containing the code for data loading, merging, renaming, and one-hot encoding.
- `report.md`: Detailed report of the data preparation phase.
- `prepared_asos_data.csv`: The final, prepared dataset ready for data exploration and analysis.
