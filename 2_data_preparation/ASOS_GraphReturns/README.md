# ASOS_GraphReturns Data Preparation

This directory is dedicated to the data preparation phase of the `ASOS_GraphReturns` dataset. The goal here is to transform raw data into a clean, merged, and analysis-ready format.

## 📊 Notebook Overview: `prepare_asos.ipynb`

| Section | Description |
|---|---|
| **Data Loading** | Loads `customer_nodes`, `event_table`, and `product_nodes` datasets (training sets) from their respective CSV files. |
| **Data Merging** | Combines the three datasets into a single, comprehensive DataFrame. Uses `event_table` as the base, merging with `customer_nodes` on `customer_id` and then with `product_nodes` on `variant_id`. |
| **Column Renaming** | Renames hashed ID columns (`hash(customerId)`, `hash(variantID)`, `hash(productID)`, `hash(supplierRef)`) to more readable names (`customer_id`, `variant_id`, `product_id`, `supplier_ref_id`). |
| **Categorical Variable Handling** | Applies one-hot encoding to remaining categorical features (`shippingCountry`, `productType`, `brandDesc`) that were not pre-encoded, ensuring numerical representation for modeling. |
| **Missing Value Check** | Performs a final check for missing values after all transformations to ensure data integrity. |
| **Data Export** | Saves the final prepared DataFrame as `prepared_asos_data.csv` for use in subsequent analysis phases. |

## 📁 Folder Structure

```
2_data_preparation/
└── ASOS_GraphReturns/
    ├── prepare_asos.ipynb  # The main data preparation notebook
    ├── report.md           # Detailed report of the data preparation process
    └── prepared_asos_data.csv # Output: The cleaned and merged dataset
```

## 🚀 How to Run

To execute the data preparation steps:

1.  **Ensure Dependencies:** Make sure you have Python and the necessary libraries installed (e.g., `pandas`, `scikit-learn`). You can install them via `pip install pandas scikit-learn`.
2.  **Navigate:** Open your terminal or command prompt and navigate to the project root directory.
3.  **Run Jupyter:** Start a Jupyter Notebook server by running `jupyter notebook`.
4.  **Open Notebook:** In the Jupyter interface, navigate to `2_data_preparation/ASOS_GraphReturns/` and open `prepare_asos.ipynb`.
5.  **Execute Cells:** Run all cells in the notebook sequentially. The notebook will load the raw data, perform the preparation steps, and save the `prepared_asos_data.csv` file in this directory.

## 📝 Notes and Assumptions

-   **Input Data Location:** This notebook assumes that the raw `.csv` data files (`customer_nodes_training.csv`, `event_table_training.csv`, `product_nodes_training.csv`) are located in `1_datasets/MIT Data Science/CSV Files/` relative to the project root.
-   **Training Data Focus:** This preparation specifically focuses on the *training* datasets. A similar process would be applied to the testing datasets for model evaluation.
-   **Hashed IDs:** The dataset uses hashed IDs for customers, products, and suppliers. These are treated as unique identifiers for merging purposes.
-   **One-Hot Encoding:** Categorical features are one-hot encoded with `drop_first=True` to prevent multicollinearity.
-   **No Complex Imputation:** Based on initial exploration, no complex missing value imputation strategies were required as the datasets were relatively clean after merging.

For a more detailed technical report on the data preparation steps and outcomes, please refer to `report.md`.