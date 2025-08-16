# ASOS Return Prediction: Results Communication

## 🌍 Project Overview

This document communicates the main findings from the ASOS Return Prediction project. It focuses on **insights, patterns, and visualizations** to help understand why products are returned and how this knowledge can be applied.

---

## 🏆 Key Findings

### Model Performance

Three models were evaluated for predicting returns:

| Model               | Accuracy | Precision | Recall | ROC AUC |
| ------------------- | -------- | --------- | ------ | ------- |
| XGBoost             | 0.742    | 0.751     | 0.798  | 0.825   |
| Logistic Regression | 0.739    | 0.749     | 0.793  | 0.820   |
| Random Forest       | 0.725    | 0.742     | 0.771  | 0.801   |

* **XGBoost** performed best in distinguishing returned vs. non-returned items.

📊 ROC AUC Comparison:

![Model ROC AUC Comparison](4_data_analysis/ASOS dataset/Models/model_roc_comparison.png)

---

### Feature Importance

The most influential predictors of returns were:

* **Customer past return rate**
* **Product return rate**
* **Shipping country**
* **Customer demographics** (smaller effect)

📊 XGBoost Feature Importance:
!\[XGBoost Feature Importance]\(4\_data\_analysis/ASOS dataset/Models/xgboost\_feature\_importance.png)

📊 Random Forest Feature Importance:
!\[Random Forest Feature Importance]\(4\_data\_analysis/ASOS dataset/Models/randomforest\_feature\_importance.png)

---

### Patterns in Returns

#### Dimensionality Reduction

* **PCA**: Showed partial separation between returned and non-returned items
  !\[PCA Plot]\(4\_data\_analysis/ASOS dataset/Models/pca\_plot.png)

* **t-SNE**: Showed more distinct clusters but still overlapping
  !\[t-SNE Plot]\(4\_data\_analysis/ASOS dataset/Models/tsne\_plot.png)

#### SHAP Analysis

* Explains individual predictions and global feature impact

Static force plot:
!\[SHAP Force Plot]\(4\_data\_analysis/ASOS dataset/Models/shap\_force\_plot.png)
Interactive version: \[SHAP Force Plot (Interactive)]\(4\_data\_analysis/ASOS dataset/Models/shap\_force\_plot.html)

---

## 📊 Data Exploration Visualizations

These charts from the initial data exploration highlight customer, product, and transaction-level patterns related to returns:

* **Shipping Countries with Highest Return Rates**
  !\[Top 10 Shipping Countries by Return Rate]\(4\_data\_exploration/ASOS dataset/Visualizations/Top%2010%20Shipping%20Countries%20by%20Return%20Rate.png)

* **Product Types with Highest Return Rates**
  !\[Top 10 Product Types by Return Rate]\(4\_data\_exploration/ASOS dataset/Visualizations/Top%2010%20Product%20Types%20by%20Return%20Rate.png)

* **Brands with Highest Return Rates**
  !\[Top 10 Brands by Return Rate]\(4\_data\_exploration/ASOS dataset/Visualizations/Top%2010%20Brands%20by%20Return%20Rate.png)

* **Return Rate by Age Group**
  !\[Return Rate by Age Group]\(4\_data\_exploration/ASOS dataset/Visualizations/return\_rate\_by\_age\_group.png)

* **Return Rate by Gender**
  !\[Return Rate by Gender]\(4\_data\_exploration/ASOS dataset/Visualizations/return\_rate\_by\_gender.png)

* **Return Rate by Premier Status**
  !\[Return Rate by Premier Status]\(4\_data\_exploration/ASOS dataset/Visualizations/return\_rate\_by\_premier.png)

* **Customer Purchase Behavior**
  !\[Sales Per Customer Distribution]\(4\_data\_exploration/ASOS dataset/Visualizations/salesPerCustomer\_distribution.png)
  !\[Returns Per Customer Distribution]\(4\_data\_exploration/ASOS dataset/Visualizations/returnsPerCustomer\_distribution.png)

* **Product Pricing & Discounts**
  !\[Average GBP Price Distribution]\(4\_data\_exploration/ASOS dataset/Visualizations/avgGbpPrice\_distribution.png)
  !\[Average Discount Value Distribution]\(4\_data\_exploration/ASOS dataset/Visualizations/avgDiscountValue\_distribution.png)
  !\[Sales Per Product Distribution]\(4\_data\_exploration/ASOS dataset/Visualizations/salesPerProduct\_distribution.png)

---

## 📈 Insights Summary

* **Customer behavior** is the strongest driver of returns.
* Certain products, brands, and regions are consistently more prone to returns.
* Returns are influenced by **complex, high-dimensional patterns**, as confirmed by PCA, t-SNE, SHAP, and exploratory visualizations.

---

## ⚖️ Limitations

* Predictions are **probabilistic**, not deterministic.
* External factors (e.g., trends, seasonality) are not included.
* Missing features such as product descriptions or fit issues limit interpretability.

---

## ✅ Conclusion

* Returns are **predictable to a useful extent** using historical customer and product behavior.
* Insights can help ASOS:

  * Improve inventory and logistics planning
  * Target high-return product categories for improvement
  * Personalize customer guidance to reduce avoidable returns

---

*This document is intended to communicate results and support decision-making, not to provide detailed modeling instructions.*
