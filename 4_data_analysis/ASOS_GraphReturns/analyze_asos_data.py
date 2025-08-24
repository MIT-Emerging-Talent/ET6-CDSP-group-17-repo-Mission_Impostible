

import pandas as pd
from sklearn.model_selection import train_test_split
import lightgbm as lgb
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create images directory if it doesn't exist
output_image_dir = 'C:/Users/ADMIN/ET6-CDSP-group-17-repo/4_data_analysis/ASOS_GraphReturns/images/'
os.makedirs(output_image_dir, exist_ok=True)

# Load the prepared data
prepared_data_path = 'C:/Users/ADMIN/ET6-CDSP-group-17-repo/2_data_preparation/ASOS_GraphReturns/prepared_asos_data.csv'
try:
    df = pd.read_csv(prepared_data_path)
    print(f"Successfully loaded prepared data from {prepared_data_path}")
except FileNotFoundError:
    print(f"Error: {prepared_data_path} not found. Please ensure the data preparation step was completed.")
    exit() # Exit if data not found

# Handle missing values by filling with the mean for numeric columns
df.fillna(df.mean(numeric_only=True), inplace=True)

# One-hot encode categorical features
categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
ids_to_exclude = ['customer_id', 'variant_id', 'product_id', 'supplier_ref_id']
categorical_cols = [col for col in categorical_cols if col not in ids_to_exclude]

if categorical_cols:
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    print(f"One-hot encoded the following columns: {categorical_cols}")


# Define features (X) and target (y)
cols_to_drop = ['customer_id', 'variant_id', 'product_id', 'supplier_ref_id', 'isReturned']
original_categorical_cols = [col for col in ['country', 'gender'] if col in df.columns]
cols_to_drop.extend(original_categorical_cols)


X = df.drop(columns=cols_to_drop, errors='ignore')
y = df['isReturned']

# Align columns between training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


# Initialize and train the LightGBM model
model = lgb.LGBMClassifier(n_estimators=50, random_state=42, n_jobs=-1, learning_rate=0.1, num_leaves=31)
print("\n--- Training LightGBM Classifier Model ---")
model.fit(X_train, y_train)
print("Model training complete.")

# Make predictions on the test set
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

print("\n--- Model Evaluation ---")
print("Classification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Predicted 0', 'Predicted 1'],
            yticklabels=['Actual 0', 'Actual 1'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.savefig(os.path.join(output_image_dir, 'confusion_matrix.png'))
print("Generated confusion_matrix.png")

# ROC Curve and AUC
fpr, tpr, _ = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)
plt.figure(figsize=(6, 5))
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.savefig(os.path.join(output_image_dir, 'roc_curve.png'))
print("Generated roc_curve.png")

# Feature Importance
importances = pd.Series(model.feature_importances_, index=X.columns)
top_features = importances.sort_values(ascending=False).head(15)
plt.figure(figsize=(10, 7))
sns.barplot(x=top_features.values, y=top_features.index, palette='viridis')
plt.title('Top 15 Features Influencing Product Returns')
plt.xlabel('Feature Importance Score')
plt.ylabel('Feature')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(os.path.join(output_image_dir, 'feature_importance.png'))
print("Generated feature_importance.png")

