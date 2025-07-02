import pandas as pd

# Load the dataset
df = pd.read_csv('1_datasets/returns_features_v2.csv')

# Display basic information about the dataset
print("Dataset Shape:")
print(df.shape)
print("\nColumn Data Types:")
df.info()
print("\nMissing Values:")
print(df.isnull().sum())
print("\nPreview of the data:")
print(df.head())
print("\nSummary statistics:")
print(df.describe())
print("\nValue counts of 'RETURN_FLAG' column:")
print(df['RETURN_FLAG'].value_counts())