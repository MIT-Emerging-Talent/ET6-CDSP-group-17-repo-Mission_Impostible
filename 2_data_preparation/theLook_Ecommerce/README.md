# 📦 TheLook E-commerce Return Data Preparation

This notebook creates a clean, modelling-ready feature set from the raw **TheLook** e-commerce data.

---

## 📑 What the Notebook Does

| Step | Action | Key Points |
|------|--------|------------|
| 1️⃣ | **Load** the four CSVs | `distribution_centers`, `order_items`, `products`, `users` |
| 2️⃣ | **Clean & Engineer** | - Flag returns (`RETURN_FLAG`)  <br>- Basket size  <br>- Discount %  <br>- Tenure, shipping latency, time features |
| 3️⃣ | **Select Columns** | Keep only the features needed for modelling |
| 4️⃣ | **Save Output** | Writes `thelook_returns_features_v2.csv` to the current folder |

> **Target variable:** `RETURN_FLAG` &nbsp;•&nbsp; `1 = returned`, `0 = kept`

---

## 📂 Folder Structure

project_root/
└─ 1_datasets/
└─ thelook_Ecommerce/
├─ distribution_centers.csv
├─ order_items.csv
├─ products.csv
└─ users.csv
└─ 2_data_preparation/
└─theLook_Ecommerce/
├─ theLook_Data_Preparation.ipynb   ← this notebook
└─ thelook_returns_features.csv  ← output

---

## 🚀 How to Run

1. Clone the repo and install requirements (`pandas`, `numpy`, `matplotlib`, `ipython` or Jupyter).
2. Open **TheLook_Data_Preparation.ipynb** in Jupyter or VS Code.
3. Run all cells.  
   You’ll see a preview of the raw tables and derived features.
4. Find the prepared CSV in the same folder at the end of the run.

---

## ⚠️ Notes & Assumptions

* Paths are **relative**—no hard-coded user directories.
* Missing timestamps are coerced to `NaT`; numeric errors are coerced to `NaN`.
* Discount % is clipped to `[0, 1]`.
* Season is derived from the purchase month using a simple month-to-season map.

---

Any questions or suggestions? Open an issue or start a discussion!