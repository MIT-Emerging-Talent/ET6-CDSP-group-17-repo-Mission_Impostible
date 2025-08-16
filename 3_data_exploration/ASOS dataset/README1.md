
# ASOS Returns Prediction: Exploratory Data Analysis Summary

This document provides a non-technical summary of the key findings from the initial exploration of the ASOS customer returns dataset. The goal of this analysis was to understand the data and identify factors that might be related to whether a purchased item is returned.

## Key Findings from the Analysis

The dataset contains information about customer transactions on ASOS, including details about the customer, the purchased product, and the transaction itself.
It has over 1.3 million entries and includes various attributes like customer ID, product ID, year of birth, shipping country, product type, brand, price, discount, and whether the item was returned.

The main goal is to predict whether an item will be returned ('isreturned').
Looking at the data, a significant portion of items are returned. Approximately 55.31% of the items in the dataset were returned, while 44.69% were not returned.
This indicates a notable return rate that the prediction model will aim to address.

Analyzing the numeric features provides insights into customer and product characteristics.
Features like 'salespercustomer' and 'returnspercustomer' show distributions that highlight variations in customer purchasing and return behavior.
The 'customerreturnrate' feature appears to have a clear relationship with the 'isreturned' label, suggesting that customers who have returned items more frequently in the past are more likely to return items in the future.
Other features like average price and discount also show some variations related to returns, indicating that product pricing and promotions might influence return decisions.

Categorical features like 'shippingcountry', 'producttype', and 'branddesc' reveal popular categories within the dataset.
The analysis shows that return rates can vary significantly across different shipping countries, product types, and brands. For example, some countries or product types might have higher or lower return rates compared to the overall average. This suggests that location and product characteristics play a role in return behavior.

We also looked at how return rates vary across different age groups.
The analysis indicates that return rates are relatively similar across the age groups of 26-35, 36-50, and 51+, with slightly lower rates observed in the 18-25 age group.
This suggests that while age might have some influence, it might not be the strongest predictor of returns compared to customer and product-specific factors.

The correlation analysis between numeric features and the return label shows that some features are more correlated with returns than others.
Notably, features related to past return behavior, such as 'customerreturnrate', show a stronger positive correlation with 'isreturned'. Other features generally show weaker correlations, suggesting that a combination of factors likely influences return decisions.

In summary, this initial exploration highlights several factors potentially related to item returns:
- **Past Customer Return Behavior:** Customers with a history of high return rates are more likely to return items.
- **Product Characteristics:** The type of product and its brand seem to influence return rates.
- **Geographic Location:** Shipping country also appears to play a role in return patterns.
- **Age Group:** While analyzed, age group appears to have a less pronounced impact on return rates compared to customer and product-specific factors.

These findings provide a foundation for building a predictive model by identifying features that are most likely to be informative for predicting returns.
