
# Customer Return Behavior Analysis

## 📊 Overview

This project explores return behavior in the `asos_merged_training.csv` dataset. The goal is to understand how often customers return products, what patterns exist across different customer groups, and which factors most influence returns.

We provide both technical and non-technical explanations, making the analysis accessible for data analysts, business stakeholders, and curious learners alike.

---

## 🧠 Non-Technical Summary

### 1. **Do people return things a lot?**
We started by looking at how many items were returned versus kept. A simple chart ([Class Distribution]) shows that **most items are *not* returned**, but some are.

### 2. **How often do customers return things?**
We looked at each customer:
- A chart called [How Many Times Customers Return Products] shows that **most customers only return items once or twice**.
- Another chart, [How Often Do Customers Return Items?], shows the *average* return rate for each customer — many people return less than half of what they buy.

### 3. **What factors affect returns?**
Some product types and customer groups return items more often. For example:
- Certain **product categories** have higher return rates.
- Customers in some **countries** return more than others.
- Return rates differ by **gender** and **age group**.

All of this is shown in charts like [Return Rate by Gender, Country, Product Type, and Age Group].

---

## 📈 Key Visualizations

- **Class Distribution: Returned vs Not Returned**  
  How many items were returned vs not returned.

- **How Many Times Customers Return Products**  
  Counts how often customers return items.

- **How Often Do Customers Return Items?**  
  Shows the average return rate per customer.

- **Top Numeric Correlations with Return**  
  Shows which numeric features (like past returns) are most related to return behavior.

- **Return Rate by Gender, Shipping Country, Product Type, Age Group**  
  Compares return rates across various categories.

---

## ⚙️ How to Run the Analysis

### 1. **Install Requirements**
Make sure Python is installed, then install the libraries:

```bash
pip install pandas seaborn matplotlib
```

### 2. **Get the Data**
Download `asos_merged_training.csv` and place it in the same folder as the script.

### 3. **Run the Script**
Use this command to run the analysis and generate visualizations:

```bash
python analysis_script.py
```

The script will print findings and open charts to visualize the results.

---

## 📄 Technical Documentation

For a detailed walkthrough of the analysis — including methods, limitations, and future suggestions — read the [documentation.md](documentation.md) file.

---

## 📌 Summary of Insights

- Most items are not returned.
- Most customers return items rarely — but a few return a lot.
- Key return indicators include:
  - Customer's past return rate (`customerReturnRate`)
  - Product's past return rate (`productReturnRate`)
  - Number of past returns per customer (`returnsPerCustomer`)
- Factors like gender, country, product type, and age group impact return likelihood.
- The target variable is imbalanced (more non-returns), which needs attention for predictive modeling.

---

## 🔮 What Could Be Next?

- Explore **feature interactions** — for example, if certain products are returned more often by certain age groups.
- Use **advanced models** (e.g., Random Forests or XGBoost) to better predict returns.
- Apply **customer segmentation** or **clustering** to find common patterns.
- Use **balancing techniques** like SMOTE if training classification models.

---

© 2025 | ASOS Return Behavior Analysis
