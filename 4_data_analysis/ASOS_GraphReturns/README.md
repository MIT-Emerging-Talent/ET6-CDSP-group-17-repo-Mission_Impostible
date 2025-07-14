# ASOS_GraphReturns Data Analysis

This directory is dedicated to the data analysis and predictive modeling phase for the `ASOS_GraphReturns` dataset. The primary goal is to build and evaluate a machine learning model to predict product returns.

## 📊 Notebook Overview: `analyze_asos.ipynb`

| Section | Description |
|---|---|
| **Data Loading** | Loads the `prepared_asos_data.csv` file, which is the output from the data preparation phase. |
| **Feature & Target Definition** | Defines the features (`X`) and the target variable (`isReturned`, `y`) for the predictive model. Excludes ID columns and any remaining non-numeric columns. |
| **Train-Test Split** | Splits the dataset into training and testing sets (80/20 split) using stratification to maintain the class balance of the target variable. |
| **Model Training** | Initializes and trains a `RandomForestClassifier` model. This model is chosen for its robustness and effectiveness in classification tasks. |
| **Model Evaluation** | Assesses the model's performance using various metrics: a classification report (precision, recall, f1-score), a confusion matrix, and the Receiver Operating Characteristic (ROC) curve with Area Under the Curve (AUC) score. |
| **Feature Importance** | Identifies and visualizes the most important features that contribute to the model's predictions, providing insights into factors influencing product returns. |

## 📁 Folder Structure

```
4_data_analysis/
└── ASOS_GraphReturns/
    ├── analyze_asos.ipynb  # The main data analysis and modeling notebook
    ├── report.md           # Detailed report of the data analysis process and results
```

## 🚀 How to Run

To execute the data analysis and modeling steps:

1.  **Ensure Dependencies:** Make sure you have Python and the necessary libraries installed (e.g., `pandas`, `scikit-learn`, `matplotlib`, `seaborn`). You can install them via `pip install pandas scikit-learn matplotlib seaborn`.
2.  **Navigate:** Open your terminal or command prompt and navigate to the project root directory.
3.  **Run Jupyter:** Start a Jupyter Notebook server by running `jupyter notebook`.
4.  **Open Notebook:** In the Jupyter interface, navigate to `4_data_analysis/ASOS_GraphReturns/` and open `analyze_asos.ipynb`.
5.  **Execute Cells:** Run all cells in the notebook sequentially. The notebook will load the prepared data, train the model, evaluate its performance, and display feature importances.

## 📝 Notes and Assumptions

-   **Input Data:** This notebook relies on the `prepared_asos_data.csv` file generated in the `2_data_preparation` phase. Ensure that the data preparation step has been successfully completed.
-   **Model Choice:** A `RandomForestClassifier` is used as a robust baseline model. Further optimization and exploration of other models could be pursued.
-   **Evaluation Metrics:** The chosen evaluation metrics (precision, recall, f1-score, confusion matrix, ROC-AUC) are standard for binary classification problems and provide a comprehensive view of model performance.
-   **Feature Importance:** The feature importance derived from the Random Forest model indicates the relative contribution of each feature to the prediction. This can guide further feature engineering or business insights.

For a more detailed technical report on the data analysis steps, model performance, and feature importance findings, please refer to `report.md`.