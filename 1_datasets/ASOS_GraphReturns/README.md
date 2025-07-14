# ASOS_GraphReturns Dataset Exploration

This directory contains the `ASOS_GraphReturns` dataset and related files, focusing on the initial exploration phase of the data science project.

## 📊 Notebook Overview: `explore_asos.ipynb`

| Section | Description |
|---|---|
| **Data Loading** | Loads `customer_nodes`, `event_table`, and `product_nodes` datasets (both training and testing sets) from their respective CSV files. |
| **Initial Inspection** | Performs a preliminary examination of each DataFrame, including checking its shape, column names, data types, and identifying any missing values. |
| **Key Observations** | Documents the content and structure of each dataset, highlighting the use of hashed IDs for linking and the presence of pre-encoded categorical features. |
| **Data Quality Assessment** | Provides an initial assessment of data consistency and completeness based on the loaded data. |

## 📁 Folder Structure

```
1_datasets/
└── ASOS_GraphReturns/
    ├── ASOS_Return.ipynb       # Original Jupyter Notebook for data loading and initial processing
    ├── DATA_DOCUMENTATION.md   # Documentation provided with the dataset
    ├── explore_asos.ipynb      # The main data exploration notebook
    └── report.md               # Detailed report of the data exploration phase
```

## 🚀 How to Run

To execute the data exploration steps:

1.  **Ensure Dependencies:** Make sure you have Python and the necessary libraries installed (e.g., `pandas`). You can install them via `pip install pandas`.
2.  **Navigate:** Open your terminal or command prompt and navigate to the project root directory.
3.  **Run Jupyter:** Start a Jupyter Notebook server by running `jupyter notebook`.
4.  **Open Notebook:** In the Jupyter interface, navigate to `1_datasets/ASOS_GraphReturns/` and open `explore_asos.ipynb`.
5.  **Execute Cells:** Run all cells in the notebook sequentially to perform the data loading and initial inspection.

## 📝 Notes and Assumptions

-   **Input Data Location:** This notebook assumes that the raw `.csv` data files are located in `1_datasets/MIT Data Science/CSV Files/` relative to the project root.
-   **Data Integrity:** Assumes the raw data files are intact and accessible.
-   **Initial Focus:** This phase focuses on understanding the raw data structure and quality before any transformations.

For a more detailed technical report on the data exploration findings, please refer to `report.md`.
