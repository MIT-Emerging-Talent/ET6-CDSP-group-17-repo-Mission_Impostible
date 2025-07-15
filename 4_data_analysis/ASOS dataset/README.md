# 🧑‍💻 ASOS Return Behavior Analysis – Technical Report

## 📁 Repository Structure

```
.
├── 01_data_preparation.ipynb   # Load + merge customer, product, and event data
├── 02_data_exploration.ipynb   # EDA and customer behavior analysis
├── 03_modeling_analysis.ipynb  # Random Forest classification modeling
├── asos_merged_training.csv    # Cleaned dataset used for all analysis
├── documentation.md            # Non-technical summary
└── README.md                   # This file
```

---

## 📌 Project Goal

Use real-world graph-based retail data (ASOS) to analyze and predict product returns, focusing on:
- Feature importance
- Customer behavior
- Return risk prediction

---

## 📊 Data Sources

Three pickled files (training):
- `event_table_training.p`: Purchases and return labels
- `customer_nodes_training.p`: Customer metadata (age, gender, etc.)
- `product_nodes_training.p`: Product metadata

---

## 🧼 Data Preparation (`01_data_preparation.ipynb`)
- Loaded all files and merged on hashed IDs
- Renamed and cleaned key columns
- Exported as `asos_merged_training.csv` for reusability

---

## 📊 Data Exploration (`02_data_exploration.ipynb`)
- Visualized class imbalance
- Calculated correlations with `isReturned`
- Analyzed return behavior by:
  - Age groups
  - Gender
  - Country
  - Day of the week
  - Customer return frequency

📌 Libraries used: `pandas`, `matplotlib`, `seaborn`

---

## 🤖 Modeling (`03_modeling_analysis.ipynb`)
- Features cleaned and converted via one-hot encoding
- Model: `RandomForestClassifier` from `scikit-learn`
- Evaluation metrics: precision, recall, F1-score
- Identified top predictors of return behavior

📌 Key features: `age`, `isMale`, `productType`, `shippingCountry`

---

## 🧪 Techniques & Rationale

- **Random Forest** was selected for its interpretability and handling of mixed-type features.
- **One-hot encoding** was used to prepare categorical variables.
- **Correlation matrix** helped identify promising features.

---

## ⚠️ Limitations

- Return reasoning is not included in dataset.
- Product size, customer reviews, and visual cues are absent.
- Time-related features (e.g., return time lag) could improve modeling.

---

## 🔁 Reproducibility

### Requirements

```bash
pip install pandas matplotlib seaborn scikit-learn
```

### To Run:

1. Download the three training `.p` files and place them in the root directory.
2. Run `01_data_preparation.ipynb` to generate `asos_merged_training.csv`
3. Open `02_data_exploration.ipynb` to explore behavior.
4. Run `03_modeling_analysis.ipynb` for machine learning insights.

---

