# Technical Documentation: Product Return Prediction Analysis

## 1. Data Description

The analysis utilizes three primary datasets provided as CSV files:
- `customer_nodes_training.csv`: Contains features related to individual customers. The key identifier column used in the analysis is `hash(customerid)`, which was standardized to `customer_id`.
- `product_nodes_training.csv`: Contains features related to individual products (variants). The key identifier column used in the analysis is `hash(variantid)`, which was standardized to `product_id`. Note that the original data also contained `hash(productid)`, but `hash(variantid)` was used for merging.
- `event_table_training.csv`: Contains records of customer-product interactions (events). The key linking columns are `hash(customerid)` and `hash(variantid)`. This table also contains the target variable, `isreturned`.

These datasets were merged based on the common customer and product identifiers to create a single comprehensive dataframe for analysis.

## 2. Data Preprocessing

The following steps were performed to preprocess the data:

- **Column Name Cleaning:** Column names across all dataframes were standardized by stripping whitespace, converting to lowercase, and replacing spaces with underscores.
- **Label Identification:** The target variable `isreturned` was identified. The distribution of the label in the training data was observed to be approximately 55.3% returns (1) and 44.7% non-returns (0).
- **Data Merging:** The `event_table_training.csv` dataframe was left-merged with `customer_nodes_training.csv` on the customer ID columns (`hash(customerid)` and `customer_id`), and then with `product_nodes_training.csv` on the product ID columns (`hash(variantid)` and `product_id`). The resulting merged dataframe had a shape of (1369133, 77).
- **Missing Value Handling:** A missingness report was generated. Columns with more than 80% missing values were dropped from the merged dataframe. For the remaining columns, missing values were handled using imputation:
    - Numerical columns were imputed using the median strategy.
    - Categorical columns were imputed using a constant value, 'missing'.
- **Feature Type Identification:** Columns were categorized into numeric and categorical types. ID columns used for merging were excluded from the feature lists used for preprocessing.
- **Preprocessing Pipelines:** Separate pipelines were defined for numerical and categorical features:
    - Numerical Pipeline: `SimpleImputer` (median) followed by `StandardScaler`.
    - Categorical Pipeline: `SimpleImputer` (constant='missing') followed by `OneHotEncoder` (`handle_unknown='ignore'`, `sparse_output=False`).
    These pipelines were combined using a `ColumnTransformer`, which was fitted on the features (`X`) and used to transform the data. The transformed feature matrix `X_trans` had a shape of (1369133, 41). The fitted preprocessor was saved as `preprocessor_train.joblib`.

## 3. Train/Validation Split

The preprocessed feature matrix (`X_trans`) and the target variable (`y`) were split into training and validation sets using `train_test_split`. A test size of 10% was used, and the split was stratified based on the target variable (`y`) to maintain the original label distribution in both sets. The random state was set to 42 for reproducibility.
- Training set shapes: `X_train.shape` (1232219, 41), `y_train.shape` (1232219,)
- Validation set shapes: `X_val.shape` (136914, 41), `y_val.shape` (136914,)
The split training and validation sets were saved as `tabular_train_val.joblib`.

## 4. Bipartite Graph Creation

A bipartite graph (`G`) was constructed using the `networkx` library to represent the interactions between customers and products.
- Nodes: Customer nodes were created from `df_customers` (bipartite=0) and product nodes from `df_products` (bipartite=1). Features from the respective dataframes (excluding ID columns and non-finite values) were added as node attributes.
- Edges: Edges were created between customer and product nodes for each event recorded in `df_events`. Each edge was assigned the `isreturned` value as an attribute (`label`).
Only customers and products present in the respective node files *and* linked by an event were included in the graph.
The resulting graph contained 487508 nodes and 50275 edges.

## 5. Technical Visualizations

The following technical visualizations are suggested to provide deeper insights into the data and the effects of preprocessing:

- **Missingness Heatmap:** A heatmap of the merged dataframe (`df`) before dropping columns to visualize the pattern and extent of missing values across features.
- **Feature Distributions (Before/After Preprocessing):**
    - Histograms or density plots for key numerical features (e.g., `yearofbirth`, `salespercustomer`, `avggbpprice`) before and after `StandardScaler` application to show the effect of scaling.
    - Bar plots or count plots for categorical features (e.g., `shippingcountry`) showing the distribution of categories and the effect of `SimpleImputer(constant='missing')`.
- **Correlation Matrix:** A heatmap showing the pairwise correlations between the numerical features after imputation and scaling.
- **Bipartite Graph Properties:**
    - Degree distribution plots for customer nodes and product nodes to understand how many events each customer/product is involved in.
    - A visualization of a small subgraph to illustrate the customer-product connection structure.

## 6. Saved Artifacts

The following processed data and objects have been saved:
- `preprocessor_train.joblib`: The fitted `ColumnTransformer` object.
- `tabular_train_val.joblib`: A tuple containing `X_train`, `X_val`, `y_train`, and `y_val`.
- `merged_events_train.joblib`: The merged dataframe (`df`) after dropping high-missingness columns but before feature transformation.

These artifacts are necessary for subsequent model training and evaluation steps.
"""
