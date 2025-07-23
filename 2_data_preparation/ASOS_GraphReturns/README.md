# Data Preparation

## 🗂 Project Overview
This repository contains the **data preparation step** of a multi-phase analysis project on e-commerce product returns using the **ASOS GraphReturns Dataset**. In this notebook, we focus on:

- Uploading and reading raw data files (.p format)
- Merging the event, customer, and product datasets on hashed IDs
- Renaming critical columns for clarity
- Saving the processed, merged dataset for downstream tasks

## 📁 Input Files
Uploaded via Google Colab interface:
- `event_table_training.p`
- `customer_nodes_training.p`
- `product_nodes_training.p`

## 🧪 Output File
- `asos_merged_training.csv` — the merged and cleaned training dataset.

## 📌 Key Steps
1. **Uploading Files** using Colab’s UI
2. **Deserialization** of `.p` files using `pd.read_pickle`
3. **Merging** tables on customer and variant hashed IDs
4. **Renaming columns** to human-readable format
5. **Saving the result** to CSV format for further use

## ✅ Dependencies
To replicate this step, ensure the following libraries are installed:
```python
import pandas as pd
import pickle
from pathlib import Path
```

You also need to run this in **Google Colab** (for the `files.upload()` widget) or adapt the code for local file reads.

## ▶️ How to Run
1. Open the `01_data_preparation.ipynb` notebook in Google Colab.
2. Upload the three `.p` files when prompted.
3. The notebook will generate `asos_merged_training.csv` for use in the next analysis step.

## 📊 Visual Summary
Here is a schematic of the merging process:

```text
[customer_nodes]      [product_nodes]
       \                   /
        \                 /
        [ event_table ]  <== merge on customerId and variantID
               |
               v
      asos_merged_training.csv
```
