# ASOS_GraphReturns Data Exploration

This directory contains files related to the exploratory data analysis (EDA) phase for the `ASOS_GraphReturns` dataset. This README provides a summary of the key findings and visualizations from the interactive exploration.

For a more detailed, interactive, and comprehensively explained analysis, please refer to the `explore_prepared_asos_interactive.ipynb` Jupyter Notebook. This notebook provides in-depth explanations for each visualization and its implications.

## Cleaned Feature Set

After the data preparation phase, the dataset contains the following key features, ready for exploration and analysis:

-   **`isReturned`**: (Target Variable) Binary indicator (0 or 1) if the product was returned.
-   **`price`**: The price of the product in GBP.
-   **`shippingCountry`**: The country to which the product was shipped (one-hot encoded during analysis).
-   **`productType`**: The type of product (e.g., 'Dress', 'Shirt', 'Jeans') (one-hot encoded during analysis).
-   **`brandDesc`**: Description of the brand (one-hot encoded during analysis).
-   **`gender`**: Gender of the customer (one-hot encoded during analysis).
-   **Other numerical features**: Various other numerical attributes derived or present in the dataset.

## Key Patterns and Visualizations

### 1. Overall Product Return Distribution

This pie chart visualizes the overall proportion of returned vs. non-returned items, providing an immediate understanding of the return rate. This distribution is crucial for understanding the class balance of our target variable.

![Overall Product Return Distribution](images/return_distribution.png)

### 2. Return Rates by Categorical Features

These bar charts show how return rates vary across different categorical features. These insights help identify which categories are associated with higher or lower return probabilities.

#### 2.1 Return Rate by Gender

![Return Rate by Gender](images/gender_return_rate.png)

#### 2.2 Return Rate by Top 10 Shipping Countries

![Return Rate by Top 10 Shipping Countries](images/country_return_rate.png)

#### 2.3 Return Rate by Top 10 Product Types

![Return Rate by Top 10 Product Types](images/product_type_return_rate.png)

### 3. Numeric Feature Distributions

#### 3.1 Distribution of Price for Returned vs. Non-Returned Items

This histogram shows the distribution of prices, differentiating between returned and non-returned items. This helps in understanding if certain price ranges are more prone to returns.

![Distribution of Price for Returned vs. Non-Returned Items](images/price_distribution.png)

### 4. Correlation Analysis

This heatmap visualizes the linear relationships between all numerical features, highlighting their correlation with the `isReturned` target variable. This helps in identifying features that have a strong linear relationship with returns.

![Correlation Matrix of Numerical Features](images/correlation_matrix.png)

## Files in this Directory:
- `explore_prepared_asos.ipynb`: Original Jupyter Notebook for data exploration.
- `explore_prepared_asos_interactive.ipynb`: Interactive Jupyter Notebook with Plotly visualizations.
- `report.md`: Detailed report of the data exploration phase.
- `images/`: Directory containing static images of the visualizations.