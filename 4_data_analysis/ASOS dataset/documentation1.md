
# ASOS Return Prediction Project: Technical Documentation

## Project Objective

The primary objective of this project is to develop and evaluate machine learning models to predict the likelihood of a purchased item being returned by an ASOS customer. From a data science perspective, this is a binary classification problem where the goal is to classify each order as either 'returned' (positive class) or 'not returned' (negative class). Accurate prediction can support business initiatives such as optimizing inventory management, personalizing customer experiences, and reducing operational costs associated with returns.

## Dataset Description

The analysis utilizes a dataset loaded from a joblib file named `/content/merged_events_train.joblib`. This dataset contains detailed information about customer purchase events.

The dataset comprises 1,369,133 records and 77 features. The features can be broadly categorized into:

*   **Numeric Features (73):** These include various numerical attributes such as customer identifiers (hashed and raw), year of birth, sales figures, return rates (at customer, product, and variant levels), average price, discount values, and potentially other quantitative metrics.
*   **Categorical Features (3):** These include object or category type features, such as shipping country.

The target variable is identified as `isreturned` or `label`, indicating whether an item was returned (1) or not (0).

## Data Preprocessing

Before training the machine learning models, the raw data underwent several preprocessing steps to handle missing values, scale numeric features, and encode categorical features.

1.  **Handling the Label Column:** The target variable, identified as `isreturned` or `label`, was separated from the features and converted to integer type.

    ```python
    label_col = "isreturned" if "isreturned" in df.columns else "label"
    X = df.drop(columns=[label_col])
    y = df[label_col].astype(int)
    ```

2.  **Identifying Feature Types:** Features were identified as either numeric or categorical based on their data types.

    ```python
    numeric_cols = X.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = X.select_dtypes(include=["object", "category"]).columns.tolist()
    ```

3.  **Preprocessing Pipelines:** Separate pipelines were constructed for numeric and categorical features using scikit-learn's `Pipeline`.

    *   **Numeric Pipeline (`num_pipeline`):**
        *   Missing values are imputed using the median strategy.
        *   Features are scaled using `StandardScaler` to have a mean of 0 and a standard deviation of 1.

        ```python
        num_pipeline = Pipeline([
            ("impute", SimpleImputer(strategy="median")),
            ("scale", StandardScaler())
        ])
        ```

    *   **Categorical Pipeline (`cat_pipeline`):**
        *   Missing values are imputed using a constant value "missing".
        *   Categorical features are one-hot encoded using `OneHotEncoder`, which converts categorical variables into a numerical format. `handle_unknown='ignore'` ensures that unseen categories during testing do not cause errors, and `sparse_output=False` returns a dense array.

        ```python
        cat_pipeline = Pipeline([
            ("impute", SimpleImputer(strategy="constant", fill_value="missing")),
            ("ohe", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
        ])
        ```

4.  **Column Transformer (`preprocessor`):** A `ColumnTransformer` was used to apply the appropriate pipeline to the correct columns. Features not specified in the `transformers` list are dropped (`remainder='drop'`).

    ```python
    preprocessor = ColumnTransformer([
        ("num", num_pipeline, numeric_cols),
        ("cat", cat_pipeline, categorical_cols)
    ], remainder="drop")
    ```

## Train/Test Split

The dataset was split into training and testing sets to evaluate the models on unseen data. A test size of 20% was used, and the split was stratified based on the target variable (`isreturned`) to ensure that both the training and testing sets have a similar proportion of returns. A fixed `random_state` was used for reproducibility.

```python
X_train_raw, X_test_raw, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
```

The preprocessing `ColumnTransformer` was then fitted on the training data (`X_train_raw`) and used to transform both the training and testing data (`X_train`, `X_test`). The names of the processed features were also extracted.

```python
X_train = preprocessor.fit_transform(X_train_raw)
X_test = preprocessor.transform(X_test_raw)
feature_names = preprocessor.get_feature_names_out()
```

## Machine Learning Models

Three different machine learning models were selected for this classification task:

*   **Random Forest:** An ensemble method that builds multiple decision trees and merges their predictions to improve accuracy and control overfitting.
*   **Logistic Regression:** A linear model used for binary classification that estimates the probability of the positive class.
*   **XGBoost (Extreme Gradient Boosting):** A powerful and efficient gradient boosting algorithm that is widely used for its performance.

```python
models = {
    "RandomForest": RandomForestClassifier(random_state=42),
    "LogisticRegression": LogisticRegression(max_iter=1000, random_state=42),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric="logloss", random_state=42)
}
```

## Model Training and Evaluation

Each model was trained on the preprocessed training data (`X_train`, `y_train`) and evaluated on the preprocessed testing data (`X_test`, `y_test`). The following classification metrics were calculated:

*   **Accuracy:** The proportion of correctly classified instances.
*   **Precision:** The proportion of correctly predicted positive instances among all instances predicted as positive.
*   **Recall:** The proportion of correctly predicted positive instances among all actual positive instances.
*   **ROC AUC:** The Area Under the Receiver Operating Characteristic Curve, which measures the model's ability to distinguish between the positive and negative classes. A higher AUC indicates better performance.

```python
results = []

for name, model in models.items():
    print(f"
🔧 Training {name}...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_proba)

    results.append({
        "Model": name,
        "Accuracy": acc,
        "Precision": prec,
        "Recall": rec,
        "ROC AUC": auc
    })
```

## Results

The performance metrics for each model are summarized in the table below:

| Model              | Accuracy | Precision | Recall | ROC AUC |
| :----------------- | :------- | :-------- | :----- | :------ |
| XGBoost            | 0.742147 | 0.751320  | 0.797869 | 0.824915|
| LogisticRegression | 0.739072 | 0.749484  | 0.793425 | 0.820280|
| RandomForest       | 0.725122 | 0.741885  | 0.771371 | 0.800798|

The results sorted by ROC AUC are:

```
                Model  Accuracy  Precision    Recall   ROC AUC
2             XGBoost  0.742147   0.751320  0.797869  0.824915
1  LogisticRegression  0.739072   0.749484  0.793425  0.820280
0        RandomForest  0.725122   0.741885  0.771371  0.800798
```

The Model ROC AUC comparison plot visually confirms these results:

![Model ROC AUC Comparison](model_roc_comparison.png)

Based on the ROC AUC, XGBoost is the best-performing model among the three evaluated.

The ROC curves for each model are shown below, illustrating their trade-off between the True Positive Rate and False Positive Rate:

![RandomForest ROC Curve](randomforest_roc_curve.png)
![LogisticRegression ROC Curve](logisticregression_roc_curve.png)
![XGBoost ROC Curve](xgboost_roc_curve.png)

## Feature Importance

Feature importance analysis helps identify which features are most influential in the model's predictions. Both RandomForest and XGBoost models provide feature importance scores.

**Top 20 Features for RandomForest:**

![RandomForest Top 20 Feature Importances](randomforest_feature_importance.png)

**Top 20 Features for XGBoost:**

![XGBoost Top 20 Feature Importances](xgboost_feature_importance.png)

For the best-performing model (XGBoost), the most important features include `num__customerreturnrate`, `cat__shippingcountry_missing`, `num__productreturnrate`, `num__ismale`, and `num__country_g`. This indicates that a customer's historical return behavior and product-specific return rates are strong predictors, along with geographic and demographic factors.

## Dimensionality Reduction for Visualization

To visualize the data and observe potential clustering of returned vs. non-returned items, dimensionality reduction techniques were applied to the test set. Due to the large size of the dataset, a limited sample was used for visualization.

### PCA (Principal Component Analysis)

PCA was used to reduce the data to 2 principal components while retaining as much variance as possible. A sample of up to 10,000 instances from the test set was used.

```python
MAX_PCA_SAMPLES = 10000

if len(X_test) > MAX_PCA_SAMPLES:
    idx_pca = np.random.choice(len(X_test), MAX_PCA_SAMPLES, replace=False)
    X_pca_input = X_test[idx_pca]
    y_pca_input = np.array(y_test)[idx_pca]
else:
    X_pca_input = X_test
    y_pca_input = y_test

pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X_pca_input)
```

The PCA plot shows some separation between the two classes, but there is significant overlap, suggesting that the return behavior is influenced by complex interactions of features that are not easily linearly separable in 2 dimensions.

![PCA: Return Clusters](pca_plot.png)

### t-SNE (t-Distributed Stochastic Neighbor Embedding)

t-SNE is a non-linear dimensionality reduction technique that is particularly good at visualizing high-dimensional data by giving each data point a location in a two or three-dimensional map. It focuses on preserving local neighborhoods. A smaller sample of up to 3,000 instances was used for t-SNE due to its computational cost.

```python
MAX_TSNE_SAMPLES = 3000

if len(X_test) > MAX_TSNE_SAMPLES:
    idx_tsne = np.random.choice(len(X_test), MAX_TSNE_SAMPLES, replace=False)
    X_tsne_input = X_test[idx_tsne]
    y_tsne_input = np.array(y_test)[idx_tsne]
else:
    X_tsne_input = X_test
    y_tsne_input = y_test

tsne = TSNE(n_components=2, perplexity=30, random_state=42)
X_tsne = tsne.fit_transform(X_tsne_input)
```

The t-SNE plot reveals more distinct clusters compared to PCA, but returned and non-returned items are still considerably intermixed, reinforcing the complexity of the prediction task.

![t-SNE: Return Clusters](tsne_plot.png)

## Conclusion and Next Steps

This technical documentation details the process of building and evaluating machine learning models for ASOS return prediction. The XGBoost model demonstrated the best performance based on ROC AUC. Feature importance analysis highlighted the significance of historical return rates and geographic/demographic factors. Dimensionality reduction visualizations confirmed the complex nature of the data distribution for the two classes.

Potential next steps could include:

*   Hyperparameter tuning for the best-performing model (XGBoost) to further optimize its performance.
*   Exploring additional features or feature engineering techniques.
*   Investigating different modeling approaches, such as deep learning models.
*   Analyzing the misclassified instances to understand where the model struggles.
*   Implementing the model for real-time prediction and integration into ASOS's systems.

