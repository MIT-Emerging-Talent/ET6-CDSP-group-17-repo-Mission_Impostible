import pandas as pd
import os

# Correct path to the raw data files
data_path = 'C:/Users/ADMIN/ET6-CDSP-group-17-repo/1_datasets/ASOS_GraphReturns/CSV Files/'

# Load the datasets
try:
    customer_nodes = pd.read_csv(os.path.join(data_path, 'customer_nodes_testing.csv'))
    event_table = pd.read_csv(os.path.join(data_path, 'event_table_training.csv'))
    product_nodes = pd.read_pickle(os.path.join(data_path, 'product_nodes_testing.p'))
    print("Successfully loaded all raw data files.")
except FileNotFoundError as e:
    print(f"Error loading data files: {e}")
    exit()

print(f"customer_nodes shape: {customer_nodes.shape}, columns: {customer_nodes.columns.tolist()}")
print(f"event_table shape: {event_table.shape}, columns: {event_table.columns.tolist()}")
print(f"product_nodes shape: {product_nodes.shape}, columns: {product_nodes.columns.tolist()}")

# Merge the dataframes
merged_df = event_table.merge(customer_nodes, on='hash(customerId)', how='left')
print(f"merged_df after first merge shape: {merged_df.shape}, columns: {merged_df.columns.tolist()}")
merged_df = merged_df.merge(product_nodes, on='hash(variantID)', how='left')
print(f"merged_df after second merge shape: {merged_df.shape}, columns: {merged_df.columns.tolist()}")

# Rename columns
merged_df.rename(columns={
    'hash(customerId)': 'customer_id',
    'hash(variantID)': 'variant_id',
    'hash(productID)': 'product_id',
    'hash(supplierRef)': 'supplier_ref_id'
}, inplace=True)

# Handle 'shippingCountry' for one-hot encoding to prevent memory issues
if 'shippingCountry' in merged_df.columns:
    # Get the top 10 most frequent countries
    top_10_countries = merged_df['shippingCountry'].value_counts().nlargest(10).index.tolist()
    # Replace countries not in the top 10 with 'Other'
    merged_df['shippingCountry_grouped'] = merged_df['shippingCountry'].apply(lambda x: x if x in top_10_countries else 'Other')
    # One-hot encode the grouped 'shippingCountry'
    merged_df = pd.get_dummies(merged_df, columns=['shippingCountry_grouped'], prefix='Country', drop_first=False)
    print("One-hot encoded 'shippingCountry' column with top 10 and 'Other' category.")
    # Drop the original 'shippingCountry' column if it's no longer needed
    merged_df.drop('shippingCountry', axis=1, inplace=True)
else:
    print("'shippingCountry' column not found for one-hot encoding.")

# Define output directory and save the prepared data
output_dir = 'C:/Users/ADMIN/ET6-CDSP-group-17-repo/2_data_preparation/ASOS_GraphReturns/'
os.makedirs(output_dir, exist_ok=True)
output_file_path = os.path.join(output_dir, 'prepared_asos_data.csv')
merged_df.to_csv(output_file_path, index=False)

print(f'Successfully created prepared data file at: {output_file_path}')