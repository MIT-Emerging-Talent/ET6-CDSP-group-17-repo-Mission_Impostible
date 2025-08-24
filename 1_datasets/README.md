# 🛍️ Returns Prediction: Graph-Based vs Tabular E-Commerce Modeling

## 📚 Table of Contents

*   [🧠 Modeling Approaches (Non-Technical Overview)](#-modeling-approaches-non-technical-overview)
    *   [A. Tabular Modeling (TheLook Dataset)](#a-tabular-modeling-thelook-dataset)
    *   [B. Graph Modeling (ASOS Dataset)](#b-graph-modeling-asos-dataset)
*   [📁 Dataset Documentation](#-dataset-documentation)
    *   [A. ASOS GraphReturns Dataset](#a-asos-graphreturns-dataset)
    *   [B. TheLook E-Commerce Dataset](#b-thelook-e-commerce-dataset)
*   [📌 Conclusion](#-conclusion)
*   [📂 Dataset Sub-directories](#-dataset-sub-directories)


This project compares two datasets and modeling methods to predict returns in e-commerce:
	1.	Graph-based method (ASOS Returns Prediction)
	2.	Tabular data method (TheLook E-Commerce)

---

## 1. 🧠 Modeling Approaches (Non-Technical Overview)

✅ Why Two Methods?

Predicting returns is key for e-commerce logistics and customer satisfaction. We tested two methods:

📦 A. Tabular Modeling (TheLook Dataset)
Each row represents one purchase. Features include product category, customer age, price,
and shipping time. We use models like Logistic Regression or XGBoost. This method is simple,
easy to interpret, and fits well with business rules.
However, it treats each transaction separately.

🧩 B. Graph Modeling (ASOS Dataset)
The data forms a graph with customers and products as nodes. Edges represent purchases,
marked as returned or not. We apply Graph Neural Networks (GNNs).
This method learns shared return patterns, like product groups or return-prone users.
It lacks time data and only includes customers who returned at least once.

---
## 2. 📁 Dataset Documentation

A. ASOS GraphReturns Dataset
- Source: OSF (Open Science Framework)
- Data: Edge list with return labels and anonymous node features
- Issues: No timestamps, only customers with returns included
- How to get it: Download from OSF: [ASOS GraphReturns Dataset on OSF](https://osf.io/c793h/)

B. TheLook E-Commerce Dataset
- Source: Kaggle (from Google BigQuery)
- Files: Four CSVs - order_items.csv, products.csv, users.csv, distribution_centers.csv
- Issues: Some missing or null timestamps, inconsistent features over time, synthetic PII used
- How to get it: Download from Kaggle: [TheLook Ecommerce Dataset](https://www.kaggle.com/code/aniqohhanahaura/thelook-dataset)

---

## 📌 Conclusion

| Model Type | Good For                     | Not Good For            |
|------------|------------------------------|------------------------|
| Tabular    | Easy to understand and use   | Finding relationships  |
| Graph      | Detecting complex patterns   | Needs dense data, harder to explain |

Both methods give useful insights into product returns. Use them alone or together for better results.

---
## 📂 Dataset Sub-directories

*   [ASOS_GraphReturns](./ASOS_GraphReturns)
*   [theLook_Ecommerce](./theLook_Ecommerce)