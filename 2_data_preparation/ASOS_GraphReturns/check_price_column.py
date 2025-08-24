import pandas as pd

# Load the product nodes data
product_nodes = pd.read_pickle('C:/Users/ADMIN/ET6-CDSP-group-17-repo/1_datasets/ASOS_GraphReturns/CSV Files/product_nodes_training.p')

# Print the columns
print(product_nodes.columns.tolist())
