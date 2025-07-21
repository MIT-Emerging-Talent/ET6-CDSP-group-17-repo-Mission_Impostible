# 🔍 E-commerce Product Return Analysis – Data Exploration

This repository documents exploratory data analysis (EDA) steps for two datasets used in product return prediction:

1. **ASOS GraphReturns Dataset**
2. **TheLook E-commerce Dataset**

These notebooks provide visual and statistical insights into return behavior, highlighting key trends across demographics, geography, and product categories.

---

## 📊 Dataset 1: ASOS GraphReturns – Customer Return Behavior Analysis

### 🗂 Overview

Explores return behavior in `asos_merged_training.csv`, focusing on:
- How often customers return products
- What types of products and customers return more
- Which features correlate most with returns

### 🧑‍💻 Non-Technical Summary

| Question | What We Found |
|---------|----------------|
| **Do people return a lot?** | Most purchases are not returned. |
| **How often do customers return?** | Most return once or twice; average return rates are low. |
| **What affects returns?** | Product type, gender, country, age all impact return rate. |

### 📈 Key Visualizations

- Class Distribution: Returned vs Not Returned
- How Many Times Customers Return Products
- How Often Do Customers Return Items?
- Return Rate by Gender, Country, Product Type, Age Group
- Top Numeric Correlations with Return (e.g., `customerReturnRate`, `productReturnRate`, `returnsPerCustomer`)

> 🧠 The return label is imbalanced — most records are "not returned".

📄 See `documentation.md` for detailed methodology, assumptions, and future steps.

---

## 📦 Dataset 2: TheLook E-commerce – Data Exploration

### 🧾 What We Did

Analyzed the cleaned dataset `thelook_returns_features.csv` to identify patterns and potential predictors for return classification.

### 🔍 Key Steps & Insights

| Step | Description |
|------|-------------|
| ✅ Data Loaded | CSV shape and data types checked; no major nulls. |
| 📊 Return Share | 10% of items returned. |
| 🧑 Gender | Return rate: Male 10.1%, Female 10.0%. Minimal difference. |
| 🍂 Season | Higher return rate in Fall. |
| 👕 Product Category | Highest in Clothing Sets (11.9%) — likely due to fit. |
| 🌍 Country | Germany (10.5%), Australia (9.6%) showed variation. |
| 🏢 Distribution Center | Houston and Savannah ~10.3% return rate. |

### 📉 Numeric Feature Distributions

- age
- discount_pct
- basket_size
- ship_latency_days
- tenure_days

No major outliers or skew observed.

### 🔥 Correlation Heatmap

Numeric variables show weak linear correlations with `RETURN_FLAG`, implying that non-linear models or categorical features will be necessary for effective modeling.

---

## 📌 Early Takeaways

- Gender does **not** significantly affect returns.
- Season and product category **do**.
- Some countries and distribution centers have higher return rates.
- Numeric features support modeling, but are not strong predictors alone.

These insights lay the foundation for building robust models and targeted interventions in the upcoming analysis phase.

---

© 2025 | E-commerce Product Return Project