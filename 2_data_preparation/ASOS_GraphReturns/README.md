# ASOS_GraphReturns Data Preparation

This directory is dedicated to the data preparation phase of the `ASOS_GraphReturns` dataset. The goal here is to transform raw data (initially in pickle format) into a clean, merged, and analysis-ready CSV file.

## 📊 Process Overview: `prepare_data.py`

| Section | Description |
|---|---|
| **Data Loading** | Loads `customer_nodes_training.p`, `event_table_training.p`, and `product_nodes_training.p` datasets from their respective pickle files. |
| **Data Merging** | Combines the three datasets into a single, comprehensive DataFrame. It uses `event_table` as the base, merging with `customer_nodes` on `hash(customerId)` and then with `product_nodes` on `hash(variantID)`. |
| **Column Renaming** | Renames the `avgGbpPrice` column to `price` for consistency. |
| **Data Export** | Saves the final prepared DataFrame as `prepared_asos_data.csv` in this directory for use in subsequent analysis phases. |

## 📁 Folder Structure

```
2_data_preparation/
└── ASOS_GraphReturns/
    ├── prepare_asos_data.py  # The main data preparation script
    ├── report.md           # Detailed report of the data preparation process
    └── prepared_asos_data.csv # Output: The cleaned and merged dataset
```

## 🚀 How to Run

To execute the data preparation steps:

1.  **Ensure Dependencies:** Make sure you have Python and the necessary libraries installed (e.g., `pandas`). You can install them via `pip install pandas`.
2.  **Navigate:** Open your terminal or command prompt and navigate to the project root directory.
3.  **Run Script:** Execute the data preparation script:
    ```bash
    python 2_data_preparation/ASOS_GraphReturns/prepare_asos_data.py
    ```
    This script will load the raw data, perform the preparation steps, and save the `prepared_asos_data.csv` file in this directory.

## 📝 Notes and Assumptions

-   **Input Data Location:** This script assumes that the raw `.p` (pickle) data files are located in `1_datasets/ASOS_GraphReturns/CSV Files/` relative to the project root.
-   **Training Data Focus:** This preparation specifically focuses on the *training* datasets. A similar process would be applied to the testing datasets for model evaluation.
-   **Hashed IDs:** The dataset uses hashed IDs for customers, products, and suppliers. These are treated as unique identifiers for merging purposes.

For a more detailed technical report on the data preparation steps and outcomes, please refer to `report.md`.