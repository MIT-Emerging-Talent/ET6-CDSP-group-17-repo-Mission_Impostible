
# Technical Documentation: ASOS Return Behavior Analysis

## 📁 Dataset

**Source**: https://osf.io/c793h/  
**File Used**: `asos_merged_training.csv`  
**Target Column**: `isReturned` (0 = not returned, 1 = returned)

## 📌 Main Questions Addressed

1. How many items are returned vs. not returned?
2. How frequently do customers return products?
3. What are the patterns of return behavior across different age groups, genders, and countries?
4. Which features are correlated with product returns?

## 🔍 Key Features Used in Exploration

- `returnsPerCustomer`
- `salesPerCustomer`
- `avgGbpPrice`
- `avgDiscountValue`
- `salesPerProduct`
- `brandDesc`
- `gender`, `age`, `shippingCountry`, `productTypeDesc`

## 🧪 Methods Used

- **Grouping and aggregation**: Used to summarize return frequency by customer.
- **Correlation matrix**: Helped identify key numerical features linked to returns.
- **Histograms and bar plots**: Used for visualizing customer behavior and class distributions.
- **Age bucketing**: Created customer age groups to understand return behavior across demographics.

## 📊 Visualizations

- Histogram of return frequency per customer
- Bar plots of return rates by:
  - Gender
  - Country
  - Product type
  - Age group
- Correlation heatmap with target variable

## ⚠️ Limitations

- Class imbalance (few returns compared to non-returns)
- Missing values in some features not imputed
- Only training data used so far (no test/validation data yet)
- Temporal patterns not explored (time-based behavior)

## 🔧 Tools

- Python
- Pandas
- Seaborn & Matplotlib

## 💡 Suggested Next Steps

- Apply classification models using selected features
- Address class imbalance using resampling techniques
- Perform feature engineering on date-based columns
- Explore social/seasonal effects on return behavior
