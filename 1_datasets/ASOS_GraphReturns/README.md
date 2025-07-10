# Predicting Customer Returns in Fashion Retail with Graph Neural Networks

##  Project Overview
This project uses the [ASOS GraphReturns dataset]([https://osf.io/c793h/](https://drive.google.com/drive/folders/1xpCMMrpNtFms7KKrCIVClTbYNZQUcSpg?usp=sharing)) to predict whether a customer will return a purchased item. We model this problem using **Graph Neural Networks (GNNs)**, which are well-suited to the relational structure of the data—customers, products, and transactions form a natural graph.

##  Why Graphs?
- Customers and products are **nodes**.
- Transactions are **edges** with features like timestamp, size, and return label.
- This forms a **heterogeneous bipartite graph**.

GNNs can learn from the **interactions** between customers and products, capturing patterns like:
- Customers who frequently return certain brands or categories.
- Products with high return rates across similar demographics.

##  Key Result
Using a GNN, we achieved:
- **F1-score**: 0.792
- **Lower cross-entropy loss** than baseline models (e.g., logistic regression, random forest)

These results are consistent with findings from [Springer’s publication](https://link.springer.com/chapter/10.1007/978-3-031-22192-7_6).

##  Limitations
- **Cold start**: New users/products lack historical data.
- **Bias**: Return reasons (e.g., sizing, color) are not always captured.
- **Graph sparsity**: Many customers interact with a few products.


## 🔗 Resources
- Dataset: [OSF Repository](https://osf.io/c793h/)


### Structure
- **event_table_training.p / event_table_testing.p**: Purchase events.
- **customer_nodes_training.p / customer_nodes_testing.p**: Customer attributes.
- **product_nodes_training.p / product_nodes_testing.p**: Product-level features.

### Key Columns
- `hash(customerId)`, `hash(variantID)`, `isReturned`
- Demographics: `yearOfBirth`, `isMale`, `shippingCountry`, `premier`
- Product attributes: `productTypeID`, `brandID`, `price`, `returnRate`

### Known Flaws
- Includes only returners → selection bias
- No timestamps for temporal analysis
- Hashed IDs limit interpretability
- Possible class imbalance

### Reproducibility
1. Download all `.p` files from OSF.
2. Merge event with customer and product nodes.
3. Add virtual nodes (optional).
4. Split into train/validation.
