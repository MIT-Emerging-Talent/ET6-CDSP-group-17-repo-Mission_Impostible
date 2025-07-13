# ASOS_GraphReturns Data Analysis

This directory contains files related to the data analysis and predictive modeling phase for the `ASOS_GraphReturns` dataset.

## Data Analysis Phase

This phase focused on building and evaluating a machine learning model to predict product returns. Key activities included:

- **Data Loading:** Loading the prepared dataset (`prepared_asos_data.csv`).
- **Feature Engineering & Target Definition:** Defining the features (X) and the target variable (`isReturned`, y) for the model.
- **Train-Test Split:** Splitting the data into training and testing sets, ensuring stratification to maintain class balance.
- **Model Training:** Training a `RandomForestClassifier` model.
- **Model Evaluation:** Assessing the model's performance using a classification report, confusion matrix, and ROC curve with AUC score.
- **Feature Importance:** Identifying and visualizing the most important features influencing product returns.

For a detailed report of the data analysis steps, model performance, and feature importance findings, please refer to `report.md` in this directory.

## Files:
- `analyze_asos.ipynb`: Jupyter Notebook containing the code for model building, training, and evaluation.
- `report.md`: Detailed report of the data analysis phase.
