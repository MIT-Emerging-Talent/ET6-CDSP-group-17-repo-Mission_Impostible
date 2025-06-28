# ASOS Returns Prediction

This project models product return behavior in an e-commerce setting using graph-based methods.

## 📊 Approach
We treat the problem as a graph where:
- Nodes = Customers & Product Variants
- Edges = Purchase interactions (labeled with return status)

### Why Graphs?
Graph Neural Networks (GNNs) learn patterns across interactions better than tabular models.

## ❗ Known Flaws
- Only includes customers who returned at least once
- No timestamps → limits sequence analysis
- Anonymized features prevent semantic interpretation

## 🔗 Data Source
[ASOS GraphReturns Dataset on OSF](https://osf.io/c793h/)

## 🏷 Git Tag
This milestone is tagged `v1.0-dataset-ready`.
