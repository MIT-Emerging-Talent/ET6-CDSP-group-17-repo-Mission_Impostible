# 🕵️‍♂️ Mission Impostible – Group 17

## ✨ Who We Are

Welcome to **Mission Impostible**, a team of emerging data scientists from around the globe who are boldly navigating the world of analytics — while quietly battling an all-too-familiar foe: **Imposter Syndrome**.

The name? A cheeky nod to how we feel sometimes. But while we may be new to the game, we’re not backing down. We’re collaborating, learning, and growing together—one dataset at a time—and we’re on a mission to tackle real-world problems with data.

---

## 🛒 Problem Background: Returns in E-commerce

Product returns are a major challenge for online retailers, costing companies **billions** annually—not just in lost sales, but also in **reverse logistics**, **inventory disruption**, **fraud**, and **environmental waste**. Managing returns impacts profitability and customer satisfaction, requiring robust data-driven solutions.

---

# 📦 Returns Prediction: Graph-Based vs Tabular E-Commerce Modeling

This project compares two advanced approaches to predicting product returns in e-commerce:

- **Graph-based modeling** (ASOS Returns Prediction)
- **Tabular data modeling** (TheLook E-Commerce)

Our goal: **Understand and predict product returns using customer, product, and transaction features—empowering smarter business decisions.**

---

## 1. 🧠 Modeling Approaches: Why Two Methods?

Predicting returns is crucial for e-commerce logistics and customer experience. We explored:

### 📦 A. Tabular Modeling (TheLook Dataset)
- **Each row = one purchase** (features: product, customer, price, shipping, etc.)
- **Models:** Logistic Regression, XGBoost
- **Strengths:** Simple, interpretable, fits business rules
- **Limitations:** Treats transactions independently

### 🧩 B. Graph Modeling (ASOS Dataset)
- **Nodes:** Customers & products
- **Edges:** Purchases (labeled as returned/not)
- **Model:** Graph Neural Networks (GNNs)
- **Strengths:** Captures shared patterns, e.g., return-prone users or products
- **Limitations:** No time data, only includes customers with returns

---

## 2. 📁 Dataset Documentation

### A. ASOS GraphReturns Dataset
- **Source:** [OSF](https://osf.io/)
- **Data:** Edge list with return labels, anonymized features
- **Notes:** No timestamps, only customers with returns
- **How to get:** Download from OSF

### B. TheLook E-Commerce Dataset
- **Source:** [Kaggle](https://www.kaggle.com/datasets/thelookecommerce/thelook-ecommerce-dataset)
- **Files:** `order_items.csv`, `products.csv`, `users.csv`, `distribution_centers.csv`
- **Notes:** Some missing timestamps, synthetic PII
- **How to get:** Download from Kaggle

---

## 📊 Summary Table

| Model Type | Good For                  | Not Good For           |
|------------|---------------------------|------------------------|
| Tabular    | Easy to use & interpret   | Finding relationships  |
| Graph      | Complex pattern detection | Needs dense data, harder to explain |

Both methods provide valuable insights—use them together for best results.

---

# 🛍️ E-commerce Product Return Analysis – Data Preparation

We engineered modeling-ready datasets for both approaches:

## 📦 ASOS GraphReturns – Data Preparation

- **Input:** `.p` files (event, customer, product nodes)
- **Process:** Merge, clean, rename columns
- **Output:** `asos_merged_training.csv`
- **How to run:** Use `01_data_preparation.ipynb` in Google Colab

## 📦 TheLook E-commerce – Data Preparation

- **Input:** Four CSVs (orders, products, users, centers)
- **Process:** Clean, engineer features (return flag, discount %, basket size, tenure, shipping latency)
- **Output:** `thelook_returns_features.csv`
- **How to run:** Use `theLookdata_preparation.ipynb` in Jupyter/VS Code

---

## 📁 Folder Structure

```
├── 01_data_preparation.ipynb
├── 02_exploratory_data_analysis.ipynb
├── 03_feature_engineering.ipynb
├── 04_modeling.ipynb
├── data
│   ├── asos_merged_training.csv
│   ├── thelook_returns_features.csv
│   ├── order_items.csv
│   ├── products.csv
│   ├── users.csv
│   └── distribution_centers.csv
├── reports
│   ├── figures
│   └── tables
└── README.md
```

---

# 📈 Data Exploration & Insights

## ASOS GraphReturns

- **Return rates:** Most purchases are not returned; most customers return only once or twice.
- **Key drivers:** Product type, gender, country, age.
- **Imbalance:** Most records are "not returned".
- **Visuals:** Return frequencies, rates by demographic, product, geography.

## TheLook E-commerce

- **Return share:** ~10% of items returned.
- **Key drivers:** Season, product category, country, distribution center.
- **Numeric features:** Weak linear correlation with returns—non-linear models needed.
- **Visuals:** Feature distributions, return rates by group.

---

# 🤖 Predictive Modeling & Results

## ASOS (Graph-Based)

- **Models:** Logistic Regression, Random Forest, GNNs
- **Top features:** Customer/product return history, product type, country
- **Accuracy:** ~75% (Random Forest)
- **Limitations:** No return reasons, only historical patterns

## TheLook (Tabular)

- **Models:** Logistic Regression (baseline), XGBoost (advanced)
- **Best ROC-AUC:** 0.655 (XGBoost)
- **Top features:** Product category, discount %, basket size, tenure
- **Insights:** High error in certain categories/geographies; numeric features alone not enough

---

# 💡 Key Takeaways

- **Graph and tabular models each reveal unique patterns.**
- **Product category, customer history, and geography are strong predictors.**
- **Combining both approaches can improve return prediction and business strategy.**

---

## 👨‍👩‍👧‍👦 Team of Imposters

- [Shadi Shahab]
- [Pyae Linn]
- [Derek Karungani]

---

## 📜 License

[MIT License](LICENSE)

---

© 2025 | Mission Impostible – E-commerce Product Return Prediction Project
