## Dataset Documentation: ASOS GraphReturns

### Source
The dataset is sourced from the ASOS GraphReturns project hosted on the Open Science Framework (OSF): https://osf.io/c793h/.

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
