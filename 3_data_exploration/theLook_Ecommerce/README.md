# 📦 TheLook E-commerce — Data Exploration

This notebook documents our first look at the cleaned feature set and highlights the main patterns we’ll investigate further in the analysis phase.

---

## 1. Data Loaded
- **File:** `thelook_returns_features.csv`  
- Shape: *rows × columns* printed in the notebook header.

---

## 2. Quick Inspection
- Checked column data types and missing-value counts.
- No major null issues; dataset is ready for analysis.

---

## 3. Overall Return Share  

<img src="images/overall.png" alt="Return Rate Donut Chart" width="400"/>

- **Returned:** 10%  
- **Kept:** 90%

---

## 4. Return Rates by Key Categories

### Gender Returns  
<img src="images/gender.png" alt="Return Rate by Gender" width="400"/>

- **Male:** 10.1%  
- **Female:** 10.0%

### Season Returns  
<img src="images/season.png" alt="Return Rate by Season" width="400"/>

- **Fall:** highest  

### Product Category Returns  
<img src="images/category.png" alt="Return Rate by Product Category" width="400"/>

- **Clothing Sets:** 11.9%  
- **Common sizing/fit** issue 

### Country Returns  
<img src="images/country.png" alt="Return Rate by Country" width="400"/>

- **Germany** 10.5%  
- **Australia** 9.6%

### Distribution Center Returns  
<img src="images/dc.png" alt="Return Rate by Distribution Center" width="400"/>

- **Houston TX**, **Savannah GA** ≈ 10.3%

---

## 5. Numeric Distributions

<img src="images/num.png" alt="Return Rate by num" width="400"/>

- `age`
- `discount_pct`
- `basket_size`
- `ship_latency_days`
- `tenure_days`

> The distributions are reasonable; no major outliers or skewed values observed.

---

## 6. Correlation Heat-map

<img src="images/heat.png" alt="Return Rate by num" width="400"/>

- Most numeric features show **weak linear correlation** with `RETURN_FLAG`.
- Confirms we’ll need **non-linear models** or **categorical features** to explain returns effectively.

---

## 7. First Observations

- **Gender** has no meaningful impact on returns.
- **Season** and **product category** affect return rates—clothing and fall show higher returns.
- **Regional trends** suggest operational or cultural return behaviour.
- **Numeric features alone aren’t predictive**, but will support a model alongside categorical data.

These insights will inform our upcoming **Data Analysis** phase, where we build models and quantify the impact of each feature.