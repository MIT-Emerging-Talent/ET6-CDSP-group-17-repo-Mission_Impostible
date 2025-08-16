
# Technical Documentation: ASOS Returns Prediction EDA

This document details the technical steps and findings from the Exploratory Data Analysis (EDA) of the ASOS customer returns dataset.

## 1. Data Loading

- The dataset was loaded from a `joblib` file named `merged_events_train.joblib` into a pandas DataFrame named `df`.
- The loaded DataFrame has a shape of (1369133, 77), indicating over 1.3 million rows and 77 columns.

## 2. Basic Data Overview

- The `df.info()` method was used to inspect the data types and non-null counts for each of the 77 columns. The dataset contains primarily `float64` (71 columns), `int64` (3 columns), and `object` (3 columns) data types.
- The first few rows of the DataFrame were displayed using `df.head()` to get a glimpse of the data structure and content.
- Missing values were identified using `df.isna().sum()`. Several columns, particularly those related to product information (`product_id`, `hash(productid)`, `producttype`, `hash(supplierref)`, `branddesc`, and associated encoded features), have a significant number of missing values (around 474,590). Customer-related features also show missing values (around 71,648).

## 3. Target Variable Analysis

- The target variable, `isreturned`, was analyzed for its distribution using `df['isreturned'].value_counts()`.
- The dataset shows an imbalanced distribution, with 757,227 returns (label 1) and 611,906 non-returns (label 0).
- A countplot was generated using `seaborn.countplot` to visualize this distribution, and the plot was saved as `return_label_distribution.png`.

## 4. Numeric Feature Analysis

- Numeric columns were selected using `df.select_dtypes(include=[np.number])`. The target variable `isreturned` was excluded from this list.
- Histograms were generated for all numeric features using `df[numeric_cols].hist` to visualize their distributions. The plots were saved as `numeric_feature_histograms.png`.
- Box plots were created using `seaborn.boxplot` to examine the relationship between the top 10 numeric features and the `isreturned` label. These plots were saved with filenames like `[feature_name]_vs_isreturned.png`.

## 5. Categorical Feature Analysis

- Categorical columns were identified using `df.select_dtypes(include=["object", "category"])`. The identified columns are `shippingcountry`, `producttype`, and `branddesc`.
- Value counts for the top 10 categories in each categorical column were printed using `.value_counts().head(10)`.
- Countplots were generated for the top 10 categories of each categorical feature using `seaborn.countplot` to visualize their distributions. These plots were saved with filenames like `[categorical_feature]_value_counts.png`.
- Stacked bar plots were created using `pd.crosstab(..., normalize='index').plot(kind='bar', stacked=True)` to visualize the proportion of returns within the top categories of each categorical feature. These plots were saved with filenames like `[categorical_feature]_vs_isreturned.png`.

## 6. Return Rate by Age Group Analysis

- Customer age was calculated by subtracting `yearofbirth` from the `current_year` (set to 2025). Rows with missing `yearofbirth` were dropped.
- Age groups were created using `pd.cut` with defined bins (18, 25, 35, 50, 100) and labels ('18-25', '26-35', '36-50', '51+').
- Potential age outliers (ages outside 10-90) were filtered out.
- The return rate (proportion of `isreturned=1`) was calculated for each age group by grouping the data and using `value_counts(normalize=True)`.
- A bar plot was generated using `seaborn.barplot` to visualize the return rate by age group, and the plot was saved as `return_rate_by_age.png`.

## 7. Correlation Analysis

- A correlation matrix was calculated for the numeric features and the target variable `isreturned` using `df[numeric_cols + [label_col]].corr()`.
- A heatmap was generated using `seaborn.heatmap` to visualize the correlation matrix, showing the pairwise correlations between features. The plot was saved as `correlation_matrix.png`.

## 8. Additional Steps

- The final DataFrame `df` was saved to a CSV file named `merged_events_train.csv` using `df.to_csv(..., index=False)`.
- Required libraries (`pandas`, `numpy`, `matplotlib`, `seaborn`, `joblib`) were installed using `pip install`.
