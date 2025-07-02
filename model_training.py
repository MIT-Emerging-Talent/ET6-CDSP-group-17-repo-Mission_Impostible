import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Load the dataset
df = pd.read_csv('1_datasets/returns_features_v2.csv')

# Handle missing values
for col in ['tenure_days', 'ship_latency_days', 'created_hour']:
    df[col].fillna(df[col].median(), inplace=True)

for col in ['brand', 'created_dayofweek']:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Convert categorical variables to dummy variables
df = pd.get_dummies(df, columns=['gender', 'country', 'category', 'department', 'brand', 'created_dayofweek', 'season'], drop_first=True)

# Define features (X) and target (y)
X = df.drop('RETURN_FLAG', axis=1)
y = df['RETURN_FLAG']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Train a logistic regression model
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train, y_train)

# Make predictions
y_pred = logreg.predict(X_test)

# Evaluate the model
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
