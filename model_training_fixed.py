
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

# First pass: get all unique category values
categorical_cols = ['gender', 'country', 'category', 'department', 'brand', 'created_dayofweek', 'season']
all_categories = {col: set() for col in categorical_cols}

df_chunks_for_cats = pd.read_csv('1_datasets/returns_features_v2.csv', chunksize=10000)
for chunk in df_chunks_for_cats:
    for col in categorical_cols:
        all_categories[col].update(chunk[col].dropna().unique())

# Initialize the model and scaler
model = SGDClassifier(loss='log_loss', max_iter=1000, tol=1e-3)
scaler = StandardScaler()

# Second pass: process each chunk and train the model
df_chunks = pd.read_csv('1_datasets/returns_features_v2.csv', chunksize=10000)

for chunk in df_chunks:
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

    # Scale the features
    X_scaled = scaler.fit_transform(X)

    # Train the model incrementally
    model.partial_fit(X_scaled, y, classes=[0, 1])

# Evaluate the model on the last chunk
y_pred = model.predict(X_scaled)

print("Confusion Matrix (on last chunk):")
print(confusion_matrix(y, y_pred))
print("\nClassification Report (on last chunk):")
print(classification_report(y, y_pred))
