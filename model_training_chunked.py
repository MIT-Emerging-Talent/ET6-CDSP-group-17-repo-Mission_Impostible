import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

# Load the dataset in chunks
chunk_size = 10000
df_chunks = pd.read_csv('1_datasets/returns_features_v2.csv', chunksize=chunk_size)

# Initialize the model and scaler
model = SGDClassifier(loss='log_loss', max_iter=1000, tol=1e-3)
scaler = StandardScaler()

# Process each chunk
for chunk in df_chunks:
    # Handle missing values
    for col in ['tenure_days', 'ship_latency_days', 'created_hour']:
        chunk[col].fillna(chunk[col].median(), inplace=True)

    for col in ['brand', 'created_dayofweek']:
        chunk[col].fillna(chunk[col].mode()[0], inplace=True)

    # Convert categorical variables to dummy variables
    chunk = pd.get_dummies(chunk, columns=['gender', 'country', 'category', 'department', 'brand', 'created_dayofweek', 'season'], drop_first=True)

    # Define features (X) and target (y)
    X = chunk.drop('RETURN_FLAG', axis=1)
    y = chunk['RETURN_FLAG']

    # Scale the features
    X_scaled = scaler.fit_transform(X)

    # Train the model incrementally
    model.partial_fit(X_scaled, y, classes=[0, 1])

# Since we can't load the whole test set, we'll evaluate on the last chunk
# In a real-world scenario, you would have a separate, held-out test set.
y_pred = model.predict(X_scaled)

# Evaluate the model
print("Confusion Matrix (on last chunk):")
print(confusion_matrix(y, y_pred))
print("\nClassification Report (on last chunk):")
print(classification_report(y, y_pred))
