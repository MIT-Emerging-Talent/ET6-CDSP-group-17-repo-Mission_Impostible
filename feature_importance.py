
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler

# First pass: get all unique category values
categorical_cols = ['gender', 'country', 'category', 'department', 'brand', 'created_dayofweek', 'season']
all_categories = {col: set() for col in categorical_cols}

df_chunks_for_cats = pd.read_csv('1_datasets/returns_features_v2.csv', chunksize=10000)
for chunk in df_chunks_for_cats:
    for col in categorical_cols:
        chunk[col].fillna(chunk[col].mode()[0], inplace=True)
        all_categories[col].update(chunk[col].unique())

# Initialize the model and scaler
model = SGDClassifier(loss='log_loss', max_iter=1000, tol=1e-3)
scaler = StandardScaler()

# Second pass: process each chunk and train the model
df_chunks = pd.read_csv('1_datasets/returns_features_v2.csv', chunksize=10000)

# Store feature names
feature_names = []

for i, chunk in enumerate(df_chunks):
    # Handle missing values
    for col in ['tenure_days', 'ship_latency_days', 'created_hour']:
        chunk[col].fillna(chunk[col].median(), inplace=True)

    for col in ['brand', 'created_dayofweek']:
        chunk[col].fillna(chunk[col].mode()[0], inplace=True)

    # Convert categorical variables to dummy variables with consistent columns
    for col in categorical_cols:
        chunk[col] = pd.Categorical(chunk[col], categories=all_categories[col])
    chunk = pd.get_dummies(chunk, columns=categorical_cols, drop_first=True)

    # Define features (X) and target (y)
    X = chunk.drop('RETURN_FLAG', axis=1)
    y = chunk['RETURN_FLAG']

    if i == 0:
        feature_names = X.columns

    # Scale the features
    X_scaled = scaler.fit_transform(X)

    # Train the model incrementally
    model.partial_fit(X_scaled, y, classes=[0, 1])

# Get feature importance
importances = model.coef_[0]

# Create a DataFrame for visualization
feature_importance_df = pd.DataFrame({'feature': feature_names, 'importance': importances})

# Sort by importance
feature_importance_df = feature_importance_df.sort_values(by='importance', ascending=False)

# Plot the feature importances
plt.figure(figsize=(12, 8))
plt.barh(feature_importance_df['feature'][:20], feature_importance_df['importance'][:20])
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Top 20 Feature Importances')
plt.gca().invert_yaxis()
plt.savefig('feature_importance.png')

print("Feature importance plot saved as feature_importance.png")
