# ASOS GraphReturns Dataset Documentation

##  Source
- Collected by ASOS, a leading online fashion retailer.
- Released via [OSF](https://osf.io/c793h/) under CC-BY 4.0 license.
- Used in [McGowan et al. (2023)](https://arxiv.org/abs/2302.14096) and [Springer 2023](https://link.springer.com/chapter/10.1007/978-3-031-22192-7_6).

##  Structure
The dataset is structured as a graph:
- **Nodes**:
  - `Customer`: ID, anonymized demographics
  - `Product`: ID, category, brand, price
- **Edges**:
  - `Transaction`: timestamp, size, return flag (1 = returned, 0 = kept)

### Example Schema

| Node Type | Attributes |
|-----------|------------|
| Customer  | customer_id, age_group, region |
| Product   | product_id, category, brand, price |
| Edge      | transaction_id, timestamp, size, return_flag |

##  Features
- Graph-based structure enables **message passing** and **representation learning**.
- Supports **edge classification** (predicting returns).
- Includes **temporal** and **categorical** features.

##  Known Issues
- **Anonymized**: No direct customer identifiers.
- **Imbalanced**: Some product categories dominate return behavior.
- **Missing values**: Some transactions lack full metadata.

## Reproducibility
To recreate the dataset:
1. Download raw files from [OSF](https://osf.io/c793h/).
2. Run `scripts/data_cleaning.py` to clean and encode features.
3. Use `scripts/split_data.py` to create train/test splits.

##  References
- [arXiv Paper](https://arxiv.org/abs/2302.14096)
- [Springer Chapter](https://link.springer.com/chapter/10.1007/978-3-031-22192-7_6)
- [GitHub Repo](https://github.com/fabon/asos-graph-returns)
