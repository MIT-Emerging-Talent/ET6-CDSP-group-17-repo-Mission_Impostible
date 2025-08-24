import pandas as pd
import os

data_path = 'C:/Users/ADMIN/ET6-CDSP-group-17-repo/1_datasets/ASOS_GraphReturns/CSV Files/'

file_names = [
    'customer_nodes_training.p',
    'event_table_training.p',
    'product_nodes_training.p'
]

loaded_data = {}

for name in file_names:
    file_path = os.path.join(data_path, name)
    try:
        loaded_data[name] = pd.read_pickle(file_path)
        print(f'Successfully loaded {name}')
    except FileNotFoundError:
        print(f'Error: {file_path} not found. Please ensure the path is correct.')
    except Exception as e:
        print(f'Error loading {name}: {e}')

customer_nodes = loaded_data['customer_nodes_training.p']
event_table = loaded_data['event_table_training.p']
product_nodes = loaded_data['product_nodes_training.p']

print('\n--- Initial DataFrames Loaded ---')
print('Customer Nodes Shape:', customer_nodes.shape)
print('Event Table Shape:', event_table.shape)
print('Product Nodes Shape:', product_nodes.shape)

merged_df = event_table.merge(customer_nodes, on='hash(customerId)', how='left')
merged_df = merged_df.merge(product_nodes, on='hash(variantID)', how='left')

merged_df.rename(columns={'avgGbpPrice': 'price'}, inplace=True)

print('\n--- Merged DataFrame Info ---')
print('Merged DataFrame Shape:', merged_df.shape)
print('Columns after merge:')
print(merged_df.columns.tolist())

# Save the prepared DataFrame for later use
output_dir = 'C:/Users/ADMIN/ET6-CDSP-group-17-repo/2_data_preparation/ASOS_GraphReturns/'
os.makedirs(output_dir, exist_ok=True)
output_file_path = os.path.join(output_dir, 'prepared_asos_data.csv')
merged_df.to_csv(output_file_path, index=False)
print(f'\nPrepared data saved to: {output_file_path}')