# ASOS_GraphReturns Data Analysis Report

## Overview
This report details the data analysis and predictive modeling performed on the `prepared_asos_data.csv` dataset. The primary objective is to build a machine learning model capable of predicting product returns and to evaluate its performance.

## Steps Performed

### 1. Data Loading
- The `prepared_asos_data.csv` file, which was the output of the data preparation phase, was loaded into a Pandas DataFrame.

### 2. Feature and Target Variable Definition
- The target variable (`y`) was defined as `isReturned`.
- Features (`X`) were defined by dropping the `isReturned` column and any remaining ID columns (`customer_id`, `variant_id`, `product_id`, `supplier_ref_id`). Any object-type columns that might have slipped through (though unlikely after one-hot encoding) were also excluded.

### 3. Train-Test Split
- The dataset was split into training and testing sets using `train_test_split` from `sklearn.model_selection`.
- A `test_size` of 0.2 (20% for testing) and `random_state=42` for reproducibility were used.
- Stratification (`stratify=y`) was applied to ensure that the proportion of returned items is maintained in both training and testing sets, addressing potential class imbalance.

### 4. Model Training (RandomForestClassifier)
- A `RandomForestClassifier` was chosen for its robustness and ability to handle complex datasets.
- The model was initialized with `n_estimators=100` (number of trees) and `random_state=42`.
- `n_jobs=-1` was used to leverage all available CPU cores for faster training.
- The model was trained on the `X_train` and `y_train` datasets.

### 5. Model Evaluation
- **Predictions:** The trained model was used to make predictions (`y_pred`) on the `X_test` dataset. Probabilities for the positive class (`y_proba`) were also obtained for ROC curve analysis.
- **Classification Report:** A classification report was generated, providing precision, recall, f1-score, and support for both classes (returned and not returned). This gives a comprehensive view of the model's performance on each class.
- **Confusion Matrix:** A confusion matrix was plotted to visualize the counts of true positives, true negatives, false positives, and false negatives. This helps in understanding where the model is making errors.
- **ROC Curve and AUC:** The Receiver Operating Characteristic (ROC) curve was plotted, and the Area Under the Curve (AUC) was calculated. The AUC provides a single metric to summarize the model's ability to distinguish between the two classes across all possible classification thresholds.

### 6. Feature Importance
- The `feature_importances_` attribute of the trained `RandomForestClassifier` was used to identify the most influential features in predicting product returns.
- The top 15 features were extracted and visualized in a bar plot, showing their relative importance scores.

## Visualizations (Conceptual Descriptions)

- **Confusion Matrix Heatmap:** A heatmap showing the counts of correctly and incorrectly classified instances for both returned and not-returned products.
- **ROC Curve:** A plot showing the trade-off between the true positive rate (sensitivity) and the false positive rate (1-specificity) at various threshold settings. The AUC score is displayed on the plot.
- **Feature Importance Bar Plot:** A horizontal bar chart displaying the top 15 features, ordered by their importance score in predicting product returns.

## Summary of Results
- The classification report, confusion matrix, and ROC curve provide a detailed assessment of the model's predictive capabilities.
- The feature importance plot highlights which aspects of customer, product, and event data are most critical in determining whether a product will be returned.

## Next Steps
- Further model tuning and optimization (e.g., hyperparameter tuning, trying other models).
- Deployment considerations for the model.
- Final reporting and presentation of findings.
