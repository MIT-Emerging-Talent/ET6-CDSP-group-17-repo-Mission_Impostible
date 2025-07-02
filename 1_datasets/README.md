🛍️ Returns Prediction: Graph-Based vs Tabular E-Commerce Modeling

This project compares two distinct datasets and modeling strategies to understand and predict return behavior in e-commerce platforms:
	1.	Graph-based approach (ASOS Returns Prediction)
	2.	Tabular data modeling (TheLook E-Commerce)

⸻

1. 🧠 Modeling Approaches (Non-Technical Overview)

✅ Why Two Methods?

Return prediction is an important task for e-commerce logistics and customer satisfaction. We explored two modeling strategies:

📦 A. Tabular Modeling (TheLook Dataset)
	•	Each row is a single purchase.
	•	Features include: product category, customer age, price, shipping latency, etc.
	•	Model used: Logistic Regression (or other classifiers like XGBoost).
	•	Advantage: Simple, interpretable, and integrates easily with business rules.
	•	Limitation: Treats each transaction in isolation.

🧩 B. Graph Modeling (ASOS Dataset)
	•	Graph structure:
	•	Nodes: Customers & Products
	•	Edges: Purchases (labeled with return = 0/1)
	•	Model used: Graph Neural Networks (GNNs)
	•	Advantage: Learns shared return patterns (e.g., product clusters, return-prone users)
	•	Limitation: No time information, and only includes customers who returned at least once.

⸻
2. 📁 Dataset Documentation

A. ASOS GraphReturns Dataset
	•	Source: OSF (Open Science Framework)
	•	Structure:
	•	Edge list of interactions with return labels
	•	Anonymized node features (no semantics)
	•	Known Flaws:
	•	No timestamps (can’t analyze order sequence or time-based behavior)
	•	Biased: Only includes customers with at least one return
	•	How to Recreate:
	•	Download the dataset from OSF: [ASOS GraphReturns Dataset on OSF](https://osf.io/c793h/)

B. TheLook E-Commerce Dataset
	•	Source: Kaggle (originally from Google BigQuery)
	•	Structure: Split into 4 CSVs:
	1.	order_items.csv (transactions)
	2.	products.csv (SKU data)
	3.	users.csv (demographics)
	4.	distribution_centers.csv (fulfillment hubs)
	•	Known Flaws:
	•	Missing or null timestamps for some shipping or return fields
	•	Not all features are consistent across time periods
	•	Synthetic PII (emails, addresses) used for demo purposes
	•	How to Recreate:
	•	Download the dataset from Kaggle: [TheLook Ecommerce Dataset](https://www.kaggle.com/code/aniqohhanahaura/thelook-dataset)

⸻

📌 Conclusion

Model Type	Suitable For	Not Ideal For
Tabular	Interpretability, fast deployment, numeric & categorical features	Capturing relationship patterns
Graph	Complex patterns, user-product co-behaviors	Requires dense data, harder to explain

Both approaches offer insight into product return behavior from different angles. Use them individually or hybridize for ensemble learning!

Questions or contributions? Open an issue or fork the repo!