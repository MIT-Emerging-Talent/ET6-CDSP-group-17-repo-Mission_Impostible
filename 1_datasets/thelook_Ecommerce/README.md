# 📦 TheLook Dataset Overview

This project uses an **anonymised e-commerce dataset** derived from Google BigQuery’s public **TheLook** sample (mirrored on Kaggle).  
The data represent real transactional activity for an online retail site and have been split into four tidy CSV files for ease of use in pandas / scikit-learn notebooks.

> **Source:** <https://www.kaggle.com/code/aniqohhanahaura/thelook-dataset>

---

## File List

| File | Rows × Cols\* | Primary Key | Grain |
|------|---------------|-------------|-------|
| `distribution_centers.csv` | ~8 × 4 | `id` | One row per fulfilment centre |
| `order_items.csv`         | ~3.1 M × 11 | `id` (line-item) | One row per SKU per order |
| `products.csv`            | ~66 K × 9 | `id` | One row per SKU |
| `users.csv`               | ~50 K × 15 | `id` | One row per registered user |

\*Row counts are approximate; they may differ slightly from your local export.

---

## Data Dictionary

<details>
<summary><strong>distribution_center.csv</strong></summary>

| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER | Surrogate key for each DC (joins to `products.distribution_center_id` & `order_items.distribution_center_id`) |
| `name` | STRING | City + state of the warehouse (e.g. “Memphis TN”) |
| `latitude` / `longitude` | FLOAT | Geo-coordinates of the DC; useful for distance calculations |
</details>

<details>
<summary><strong>order_items.csv</strong></summary>

| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER | Unique line-item ID |
| `order_id` | INTEGER | Parent order (one order can have many items) |
| `user_id` | INTEGER | Customer who placed the order (links to `users.id`) |
| `product_id` | INTEGER | SKU purchased (links to `products.id`) |
| `inventory_item_id` | INTEGER | Internal stock-keeping key |
| `status` | STRING | Fulfilling state: `Shipped`, `Cancelled`, … |
| `created_at` | TIMESTAMP | When the item was placed in the cart / paid |
| `shipped_at`, `delivered_at`, `returned_at` | TIMESTAMP | Logistics life-cycle stamps (null if not yet occurred) |
| `sale_price` | FLOAT | Price paid after discount |
</details>

<details>
<summary><strong>products.csv</strong></summary>

| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER | SKU identifier |
| `cost` | FLOAT | Unit cost to retailer |
| `category` | STRING | High-level category (e.g. *Swim*, *Tops*) |
| `name` | STRING | Full merchandise name |
| `brand` | STRING | Brand / label |
| `retail_price` | FLOAT | MSRP before discount |
| `department` | STRING | Men / Women / Kids etc. |
| `sku` | STRING | Hash-style merch code |
| `distribution_center_id` | INTEGER | Default warehouse fulfilling this SKU |
</details>

<details>
<summary><strong>users.csv</strong></summary>

| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER | Customer ID |
| `first_name`, `last_name`, `email` | STRING | PII fields (hash-like but useful for demos) |
| `age` | INTEGER | Age at account creation |
| `gender` | STRING | `M`, `F`, or `NULL` |
| `state`, `street_address`, `postal_code`, `city`, `country` | STRING | Shipping location |
| `latitude`, `longitude` | FLOAT | Geo-coordinates of primary address |
| `traffic_source` | STRING | Acquisition channel (SEO, Facebook, …) |
| `created_at` | TIMESTAMP | Account registration date |
</details>

---

## Suggested Feature Groups for Return-Propensity Models

| Aspect | Example Columns |
|--------|-----------------|
| **Customer** | `gender`, `age`, `country`, *tenure (days between user & order)* |
| **Product**  | `category`, `brand`, `retail_price`, `cost`, *discount %* |
| **Order**    | `basket_size`, `sale_price`, `distribution_center_id`, `ship_latency_days` |
| **Temporal** | `created_hour`, `created_dayofweek`, `season` |

---

## Licence & Privacy

- TheLook data are governed by Google Cloud’s **public-dataset terms** (freely available for research & demo purposes).  
- All personal information is **synthetic or anonymised**; no real customer identities are exposed.

---
