# Data Preparation

## 🗂 Project Overview
This repository contains the **data preparation step** of a multi-phase analysis project on e-commerce product returns using the [**ASOS GraphReturns Dataset**](https://drive.google.com/drive/folders/1xpCMMrpNtFms7KKrCIVClTbYNZQUcSpg?usp=sharing). In this notebook, we focus on:

- Uploading and reading raw data files (.p format)
- Converting the .p files to CSV format
- Merging the event, customer, and product datasets on hashed IDs
- Renaming critical columns for clarity
- Saving the processed, merged dataset for downstream tasks

## 📁 Input Files
Uploaded via Google Colab interface:
- `event_table_training.csv`
- `customer_nodes_training.csv`
- `product_nodes_training.csv`

## 🧪 Output File
- `asos_merged_training.csv` merged and cleaned training dataset &  Saved merged graph data as: `merged_events_train.joblib`.
1.  **Customer Information:** Details about our customers, such as their age range, gender, where they live, and past purchase and return history.
2.  **Product Information:** Details about the products, including their type, brand, price, and past sales and return rates.
3.  **Event Information:** Records of every time a customer interacts with a product, specifically whether the product was eventually returned or not. This is the key piece of information we want to predict.

By linking the event information with the customer and product details, we created a comprehensive dataset for our analysis.

## Key Steps of the Analysis

Here's how we approached the analysis:

1.  **Getting the Data Ready:** We started by cleaning up the data from the three sources. This involved making sure names were consistent and handling any missing information that could cause problems later on.
2.  **Bringing Information Together:** We combined the customer, product, and event information into one large dataset. This allowed us to see all the relevant details about each customer-product interaction in one place.
3.  **Preparing for Prediction:** We transformed the combined data into a format suitable for a prediction model. This included converting different types of information (like categories) into numbers and scaling everything so that no single piece of information unfairly influenced the model. We then split this prepared data into two sets: one for the model to learn from (training data) and one to test how well it performs on new, unseen data (testing data).
4.  **Mapping Connections:** We built a special kind of map, called a bipartite graph or network, that shows the connections between customers and the products they interacted with. This network helps us understand relationships and patterns that might not be obvious from just looking at the individual data tables.

## What We Found

So far, we have successfully completed the initial steps of preparing the data for analysis and model building. We've:

*   Successfully combined information from the customer, product, and event data sources.
*   Cleaned up column names and handled a significant amount of missing data by removing features with too much missing information and filling in gaps for others.
*   Built a network showing connections between customers and products based on their interactions.

## Next Steps

The next step is to train a predictive model using the prepared data and the customer-product network to predict the likelihood of a return. This analysis can ultimately help businesses make better decisions, such as improving product descriptions, targeting customers more effectively, or optimizing return processes.
"""

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
asos_merged_training.csv & merged_events_train.joblib
```
