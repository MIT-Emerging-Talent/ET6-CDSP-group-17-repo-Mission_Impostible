# 📄 documentation.md – Data Preparation Phase

## 🧠 Non-Technical Summary
In this step, we combined three different datasets into one cohesive table to make our data easier to work with in subsequent analysis stages. These datasets include records of customer events, customer details, and product features. Merging them lets us answer questions like:

- Which customers are returning items?
- Which products are more likely to be returned?

### 🎯 What We’re Sure About
- The merging process worked without errors
- We confirmed that hashed keys were successfully used to join the datasets
- The output file was generated and saved correctly

### ⚠️ What Might Introduce Error
- If any `.p` file has mismatched keys, some data rows may be lost in the merge
- The dataset only includes training data, not full customer histories

## ⚙️ Technical Description
### Step 1: Upload Raw Pickled Files
We use Google Colab’s `files.upload()` method to import the training `.p` files manually. These are serialized with Python's pickle module and need to be loaded using `pd.read_pickle()`.

### Step 2: Merge DataFrames
We used Pandas `merge()` to join:
- `event_table` with `customer_nodes` on `hash(customerId)`
- The resulting DataFrame with `product_nodes` on `hash(variantID)`

### Step 3: Clean Column Names
Renaming `hash(customerId)` ➝ `customer_id` and `hash(variantID)` ➝ `variant_id` improves readability for downstream work.

### Step 4: Export Clean Data
The merged DataFrame is saved as `asos_merged_training.csv` using `Path().resolve()` to confirm the full save path.

## 🔁 Possible Alternative Approaches
- Use hashing validation to ensure key integrity before merging
- Add logs or counters to catch dropped rows
- Integrate error handling with try/except blocks around `read_pickle`

## 💾 Script Summary
```python
import pandas as pd
from pathlib import Path

# Load files
with open("event_table_training.p", "rb") as f:
    event = pd.read_pickle(f)
with open("customer_nodes_training.p", "rb") as f:
    cust = pd.read_pickle(f)
with open("product_nodes_training.p", "rb") as f:
    prod = pd.read_pickle(f)

# Merge and rename
merged = event.merge(cust, on="hash(customerId)")\
               .merge(prod, on="hash(variantID)")
merged.rename(columns={"hash(customerId)": "customer_id", "hash(variantID)": "variant_id"}, inplace=True)

# Save
merged.to_csv("asos_merged_training.csv", index=False)
```
