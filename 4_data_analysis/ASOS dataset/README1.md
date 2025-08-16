
# ASOS Return Prediction Project

## Project Overview

This project aims to build a machine learning model to predict whether a customer will return an item purchased from ASOS. By accurately predicting returns, ASOS can potentially optimize inventory, reduce costs associated with returns, and improve the customer experience.

## The Data

The analysis uses a dataset containing various information related to customer purchases. This includes:

*   **Customer Information:** Details about the customer, such as a unique identifier and year of birth.
*   **Product Information:** Details about the purchased item, including its unique identifier, brand, and type.
*   **Historical Behavior:** Aggregated information about the customer's and product's past return rates and sales.
*   **Order Details:** Information related to the specific purchase event.

Before training the models, the data was cleaned and prepared. This involved handling missing information and transforming some data into a format suitable for the machine learning models.

## Our Approach: Using Machine Learning

To predict returns, we trained several machine learning models on the prepared data. These models learn patterns from past purchases and returns to make predictions on new orders. We compared the performance of three different models:

*   **Random Forest:** An ensemble model that combines multiple decision trees.
*   **Logistic Regression:** A simpler model that estimates the probability of return based on the input features.
*   **XGBoost:** A powerful gradient boosting model known for its high performance.

## Model Performance

We evaluated the models based on how well they could distinguish between orders that would be returned and those that wouldn't. A key metric for this is the **ROC AUC** (Receiver Operating Characteristic Area Under the Curve). In simple terms, a higher ROC AUC means the model is better at correctly ranking potential returns higher than non-returns. An AUC of 0.5 is no better than random guessing, while an AUC of 1.0 is a perfect model.

Here's how the models performed:

![Model ROC AUC Comparison](model_roc_comparison.png)

As you can see, the **XGBoost** model achieved the highest ROC AUC, indicating it is the best-performing model for this prediction task among the ones we tested.

## What Influences Returns? (Feature Importance)

Understanding which factors the models consider most important helps us gain insights into why items are returned. The XGBoost model, being the best performer, highlighted several key features:

![XGBoost Top 20 Feature Importances](xgboost_feature_importance.png)

The most important feature by a significant margin is the **`num__customerreturnrate`**. This makes intuitive sense – customers who have returned items frequently in the past are more likely to return items in the future. Other important factors include:

*   **`cat__shippingcountry_missing`**: Indicates if the shipping country information is missing, which could be related to certain return behaviors or data collection issues.
*   **`num__productreturnrate`**: Products that are frequently returned by other customers are also more likely to be returned.
*   **`num__ismale`**: Gender appears to have some influence on return behavior.
*   **`num__country_g` / `cat__shippingcountry_Country_G`**: Specific countries seem to have different return patterns.

These insights suggest that both customer-specific behavior and product characteristics, along with shipping location, play a crucial role in predicting returns.

## Visualizing the Data

To get a better sense of how the different orders relate to each other based on their features, we used dimensionality reduction techniques to visualize the data in two dimensions.

**PCA (Principal Component Analysis):**

![PCA: Return Clusters](pca_plot.png)

PCA tries to find the main directions of variation in the data. This plot shows some separation between returned (1) and non-returned (0) items, although there is significant overlap, suggesting that predicting returns is a complex task.

**t-SNE (t-Distributed Stochastic Neighbor Embedding):**

![t-SNE: Return Clusters](tsne_plot.png)

t-SNE is another technique that tries to preserve the local relationships between data points. This plot shows more distinct clusters, but again, the returned and non-returned items are mixed, indicating that while there are patterns, they are not easily separable in two dimensions based on these features alone.

## Conclusion

This project successfully built and evaluated machine learning models to predict ASOS item returns. The XGBoost model showed the best performance, and the analysis of feature importance confirmed that historical return rates are strong indicators of future returns. These findings can inform strategies to reduce returns and improve business operations.

