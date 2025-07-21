# 🛍️ E-commerce Product Return Analysis – Data Preparation

This repository contains data preparation workflows for two e-commerce datasets used in product return prediction projects:

1. **ASOS GraphReturns Dataset**
2. **TheLook E-commerce Dataset**

Both notebooks clean, merge, and engineer modeling-ready datasets for downstream machine learning tasks such as return classification.

---

## 📦 Dataset 1: ASOS GraphReturns – Data Preparation

### 🗂 Overview

This phase prepares the **ASOS GraphReturns** training dataset by merging event, customer, and product node tables into a single structured CSV for modeling.

### 📁 Input Files

Uploaded via Google Colab interface:
- `event_table_training.p`
- `customer_nodes_training.p`
- `product_nodes_training.p`

### 🧪 Output File
- `asos_merged_training.csv` — the merged and cleaned training dataset.

### 📌 Key Steps

| Step | Description |
|------|-------------|
| 📥 Upload | Use `files.upload()` in Google Colab to load `.p` files |
| 📦 Deserialize | Load files with `pd.read_pickle` |
| 🔗 Merge | Join tables on `customer_id_hashed` and `variant_id_hashed` |
| 🏷️ Rename | Convert hashed and cryptic column names into human-readable ones |
| 💾 Save | Export merged dataset to `.csv` for analysis |

### ✅ Dependencies

- `pandas`
- `pickle`
- `pathlib`

> ⚠️ Run in **Google Colab** for compatibility with the file upload widget, or adapt to local workflows.

### ▶️ How to Run

1. Open `01_data_preparation.ipynb` in **Google Colab**.
2. Upload the `.p` files when prompted.
3. The notebook will output `asos_merged_training.csv`.

### 📊 Merging Process Diagram

```
[customer_nodes]      [product_nodes]
       \                   /
        \                 /
        [ event_table ]  <== merge on customerId and variantID
               |
               v
     asos_merged_training.csv
```

---

## 📦 Dataset 2: TheLook E-commerce – Data Preparation

### 📑 What This Notebook Does

Prepares a clean feature set from **TheLook e-commerce** dataset with return labels and engineered features.

### 📁 Input Files

Located under `1_datasets/thelook_Ecommerce/`:
- `distribution_centers.csv`
- `order_items.csv`
- `products.csv`
- `users.csv`

### 🧪 Output File
- `thelook_returns_features.csv` — modeling-ready feature set with `RETURN_FLAG` as the target.

### 📌 Key Steps

| Step | Action | Description |
|------|--------|-------------|
| 1️⃣ | Load CSVs | Read 4 raw data files |
| 2️⃣ | Clean & Engineer | Add features like return flag, discount %, basket size, tenure, and shipping latency |
| 3️⃣ | Select Columns | Retain only necessary features for modeling |
| 4️⃣ | Save Output | Write to `thelook_returns_features.csv` |

### 🎯 Target Variable

- `RETURN_FLAG`  
  - `1` = returned  
  - `0` = kept

### 🚀 How to Run

1. Clone the repository and install required libraries:
   ```bash
   pip install pandas numpy matplotlib ipython
   ```
2. Open `TheLook_Data_Preparation.ipynb` in Jupyter Notebook or VS Code.
3. Run all cells.
4. Check the output file in `2_data_preparation/theLook_Ecommerce/`.

### ⚠️ Notes & Assumptions

- Relative paths used—no hardcoded user directories.
- Missing timestamps → `NaT`; numeric errors → `NaN`.
- `discount_percent` clipped to range `[0, 1]`.
- `season` feature derived from month using a simple mapping.

---

## 📁 Folder Structure

```
project_root/
│
├── 1_datasets/
│   └── thelook_Ecommerce/
│       ├── distribution_centers.csv
│       ├── order_items.csv
│       ├── products.csv
│       └── users.csv
│
├── 2_data_preparation/
│   ├── asos_graphreturns/
│   │   └── 01_data_preparation.ipynb
│   └── thelook_Ecommerce/
│       ├── TheLook_Data_Preparation.ipynb
│       └── thelook_returns_features.csv
│
└── README.md  ← (You are here)
```

---

## 📬 Contact

For questions or collaboration, feel free to open an issue or submit a pull request.

---

## 📜 License

This project is for educational and research purposes. Refer to individual dataset licenses and terms of use before commercial application.