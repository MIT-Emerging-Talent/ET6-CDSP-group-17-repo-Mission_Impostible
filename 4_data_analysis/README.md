
# ASOS & TheLook E-commerce Product Return Analysis

This directory documents the advanced analysis and predictive modeling for two e-commerce return datasets: **ASOS GraphReturns** and **TheLook E-commerce**. Both projects share the goal of understanding and predicting product returns using customer, product, and transaction features.

---

## 📦 ASOS Product Return Analysis

### 📊 Goal
Predict whether a product will be returned based on customer behavior, product characteristics, and transaction features using the ASOS GraphReturns dataset.

### 📂 Folder Structure
```
4_data_analysis/
├── ASOS dataset/
│   └── Visualizations/
│       ├── return_frequency.png
│       ├── return_rate_distribution.png
│       ├── return_rate_by_age_group.png
│       ├── confusion_matrix_logistic.png
│       ├── confusion_matrix_rf.png
│       ├── feature_importance_logistic.png
│       ├── feature_importance_rf.png
│       ├── Top 10 Shipping Countries by Return Rate.png
│       ├── Top 10 Product Types by Return Rate.png
│       ├── Top 10 Brands by Return Rate.png
│       └── [...others]
├── asos_return_analysis.ipynb
├── README.md
└── documentation.pdf

```
### 🔍 Key Insights

- **High return rates** by specific product types, brands, and countries.
- **Customer history** (e.g., number of past returns) is a strong predictor.
- Gender, age group, and premier status play minor roles.
- Logistic Regression and Random Forest used for classification.
- Visuals: return frequencies, confusion matrices, feature importances.


### 📊 Key Predictive Features

| **Feature**             | **Role in Return Prediction** | **Interpretation**                                 |
|-------------------------|-------------------------------|----------------------------------------------------|
| `customerReturnRate`    | Strong                        | Frequent returners continue returning              |
| `productReturnRate`     | Strong                        | Certain products are repeatedly returned           |
| `returnsPerCustomer`    | Strong                        | Historical behavior is predictive                  |
| `productType`           | Moderate                      | Some types have sizing/fit issues                  |
| `country`               | Moderate                      | Cultural/operational differences                   |
| `gender`                | Weak to moderate              | Not consistent across categories                   |
| `age`                   | Weak to moderate              | Slight increase in returns among younger users     |


### 🔍 Limitations
- Missing return reasons & product fit info.
- Patterns are historical; customer behavior may change.
- Accuracy ~75% (Random Forest).

---

## 🛍️ TheLook E-commerce Return Prediction

### 📊 Analysis Workflow (12 Steps)
1. Data loading & feature checks
2. Feature engineering (minimal)
3. Logistic Regression (baseline)
4. XGBoost modeling (advanced)
5. Model evaluation: ROC, F1, precision/recall
6. Feature importance (XGBoost & SHAP)
7. Summary of key findings
8. Exploratory Data Analysis
9. Error diagnostics by category & geography
10. Robustness checks (cross-validation)
11. SHAP-based interpretability
12. Model improvement suggestions

### 🎯 Model Results
| Model              | ROC-AUC (CV) | F1-score |
|-------------------|--------------|----------|
| Logistic Regression | 0.499 ± 0.003 | Low      |
| XGBoost            | 0.655 ± 0.004 | Higher   |

### 💡 Key Features
- Product Category (strongest predictor)
- Discount %, Basket Size, Tenure
- Seasonal & regional return patterns
- High error rates in Underwear, Plus sizes, Japan

### 📈 Data Overview
- 180,952 records, 18 features
- Target: RETURN_FLAG (10% positive class)
- Missing data in: bin, ship_latency_days, tenure_days

### 📊 Visuals Generated
- ROC, PR curves
- Feature distributions (by return status)
- SHAP summary/dependence plots
- Confusion matrices & learning curves

### 💼 Recommendations
- Improve sizing/fit for high-return categories
- Target interventions for new customers & high-risk geographies
- Regularly monitor and retrain models

---

## 🔧 Technical Requirements

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost shap
```

---

## 📝 Notes

- Stratified train-test split used for fair evaluation.
- Class imbalance handled via model weighting.
- SHAP used for transparency.
- Cross-validation for all reported metrics.

---

© 2025 | ASOS & TheLook E-commerce Return Prediction Project
