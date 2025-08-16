# 🛍️ ASOS & TheLook E-commerce Product Return Analysis

This repository documents advanced analysis and predictive modeling for two e-commerce datasets:  
- **ASOS GraphReturns Dataset**  
- **TheLook E-commerce Dataset**

Both projects aim to understand and predict product returns using customer, product, and transaction features.

---

## 📦 ASOS Product Return Analysis

This project uses the [ASOS GraphReturns Dataset](https://osf.io/c793h/) to predict whether a customer will return a purchased item. With over 1.3 million records, the goal is to reduce return-related costs and improve customer experience.

###  Modeling & Results

Three models were evaluated using ROC AUC:

| Model               | Accuracy | Precision | Recall | ROC AUC |
|--------------------|----------|-----------|--------|---------|
| XGBoost            | 0.742    | 0.751     | 0.798  | 0.825   |
| Logistic Regression| 0.739    | 0.749     | 0.793  | 0.820   |
| Random Forest      | 0.725    | 0.742     | 0.771  | 0.801   |



### 🔍 Key Predictive Features

| **Feature**             | **Role in Return Prediction** | **Interpretation**                                 |
|-------------------------|-------------------------------|----------------------------------------------------|
| `customerReturnRate`    | Strong                        | Frequent returners continue returning              |
| `productReturnRate`     | Strong                        | Certain products are repeatedly returned           |
| `returnsPerCustomer`    | Strong                        | Historical behavior is predictive                  |
| `productType`           | Moderate                      | Some types have sizing/fit issues                  |
| `country`               | Moderate                      | Cultural/operational differences                   |
| `gender`                | Weak to moderate              | Not consistent across categories                   |
| `age`                   | Weak to moderate              | Slight increase in returns among younger users     |



### ⚠️ Limitations

- Missing shipping data  
- External factors (e.g., fashion trends) not included  
- Predictions are probabilistic

### ✅ Impact

- Smarter inventory planning  
- Improved sizing guidance  
- Reduced logistics costs
### 📂 How to Run the Project

1. Download the dataset from the [OSF ASOS Dataset](https://osf.io/c793h/)  
2. Run the provided script: `ASOS_Data_Analysis.ipynb`  
3. Artifacts (plots, metrics, SHAP feature importance, predictions) are saved in the `Models` folder

---

## 🛍️ TheLook E-commerce Return Prediction

### 📊 Analysis Workflow

1. Data loading & feature checks  
2. Feature engineering  
3. Logistic Regression (baseline)  
4. XGBoost modeling (advanced)  
5. Model evaluation: ROC, F1, precision/recall  
6. Feature importance (XGBoost & SHAP)  
7. Summary of key findings  
8. Exploratory Data Analysis  
9. Error diagnostics by category & geography  
10. Robustness checks (cross-validation)  
11. Model improvement suggestions  

---

### 🎯 Model Results

| Model               | ROC-AUC (CV) | F1-score |
|--------------------|--------------|----------|
| Logistic Regression| 0.499 ± 0.003| Low      |
| XGBoost            | 0.655 ± 0.004| Higher   |

---

### 💡 Key Features

- Product Category (strongest predictor)  
- Discount %, Basket Size, Tenure  
- Seasonal & regional return patterns  
- High error rates in Underwear, Plus sizes, Japan  

---

### 📈 Data Overview

- 180,952 records, 18 features  
- Target: RETURN_FLAG (10% positive class)  
- Missing data in: bin, ship_latency_days, tenure_days  

---

### 📊 Visuals Generated

- ROC, PR curves  
- Feature distributions (by return status)  
- Confusion matrices & learning curves  

---

### 💼 Recommendations

- Improve sizing/fit for high-return categories  
- Target interventions for new customers & high-risk geographies  
- Regularly monitor and retrain models  

---

## 🔧 Technical Requirements

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost shap
