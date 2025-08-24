import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Create images directory if it doesn't exist
output_image_dir = 'C:/Users/ADMIN/ET6-CDSP-group-17-repo/3_data_exploration/ASOS_GraphReturns/images/'
os.makedirs(output_image_dir, exist_ok=True)

# Load the prepared data
prepared_data_path = 'C:/Users/ADMIN/ET6-CDSP-group-17-repo/2_data_preparation/ASOS_GraphReturns/prepared_asos_data.csv'
try:
    df = pd.read_csv(prepared_data_path)
    print(f"Successfully loaded prepared data from {prepared_data_path}")
except FileNotFoundError:
    print(f"Error: {prepared_data_path} not found. Please ensure the data preparation step was completed.")
    exit() # Exit if data not found

print("--- Initial Data Overview ---")
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print("\n--- Data Info ---")
df.info()
print("\n--- Missing Values ---")
print(df.isnull().sum()[df.isnull().sum() > 0])
print("\n--- First 5 Rows ---")
print(df.head())

return_counts = df['isReturned'].value_counts()
return_percentage = df['isReturned'].value_counts(normalize=True) * 100
print(f"Value Counts for isReturned:\n{return_counts}")
print(f"\nPercentage of Returns:\n{return_percentage}")
fig = px.pie(names=['Not Returned (0)', 'Returned (1)'],
             values=return_counts.values,
             title='Overall Product Return Distribution',
             hole=0.3)
fig.update_traces(textinfo='percent+label', pull=[0, 0.1])
fig.write_image("C:/Users/ADMIN/ET6-CDSP-group-17-repo/3_data_exploration/ASOS_GraphReturns/images/return_distribution.png")
print("Generated return_distribution.png")

if 'isMale' in df.columns:
    gender_return_rate = df.groupby('isMale')['isReturned'].mean().reset_index()
    gender_return_rate['isMale'] = gender_return_rate['isMale'].map({0: 'Female', 1: 'Male'})
    fig = px.bar(gender_return_rate, x='isMale', y='isReturned',
                 title='Return Rate by Gender',
                 labels={'isMale': 'Gender', 'isReturned': 'Average Return Rate'},
                 text=gender_return_rate['isReturned'].apply(lambda x: f'{x:.2%}'))
    fig.update_traces(texttemplate='%{text:.2%}', textposition='outside')
    fig.update_layout(xaxis_tickangle=-45)
    fig.write_image("C:/Users/ADMIN/ET6-CDSP-group-17-repo/3_data_exploration/ASOS_GraphReturns/images/gender_return_rate.png")
    print("Generated gender_return_rate.png")
else:
    print("'isMale' column not found for gender analysis.")

country_cols = [col for col in df.columns if col.startswith('Country_') and col != 'Country_Other']
if country_cols:
    country_return_rates = {col.replace('Country_', ''): df[df[col] == 1]['isReturned'].mean() for col in country_cols}
    country_return_rates_series = pd.Series(country_return_rates).sort_values(ascending=False).head(10)
    fig = px.bar(x=country_return_rates_series.index, y=country_return_rates_series.values,
                 title='Return Rate by Top 10 Shipping Countries',
                 labels={'x': 'Country', 'y': 'Average Return Rate'},
                 text=country_return_rates_series.values)
    fig.update_traces(texttemplate='%{text:.2%}', textposition='outside')
    fig.update_layout(xaxis_tickangle=-45)
    fig.write_image("C:/Users/ADMIN/ET6-CDSP-group-17-repo/3_data_exploration/ASOS_GraphReturns/images/country_return_rate.png")
    print("Generated country_return_rate.png")
else:
    print("No 'Country_X' columns found for country analysis.")

product_type_cols = [col for col in df.columns if col.startswith('productType_') and col != 'productType_Other']
if product_type_cols:
    product_type_return_rates = {col.replace('productType_', ''): df[df[col] == 1]['isReturned'].mean() for col in product_type_cols}
    product_type_return_rates_series = pd.Series(product_type_return_rates).sort_values(ascending=False).head(10)
    fig = px.bar(x=product_type_return_rates_series.index, y=product_type_return_rates_series.values,
                 title='Return Rate by Top 10 Product Types',
                 labels={'x': 'Product Type', 'y': 'Average Return Rate'},
                 text=product_type_return_rates_series.values)
    fig.update_traces(texttemplate='%{text:.2%}', textposition='outside')
    fig.update_layout(xaxis_tickangle=-45)
    fig.write_image("C:/Users/ADMIN/ET6-CDSP-group-17-repo/3_data_exploration/ASOS_GraphReturns/images/product_type_return_rate.png")
    print("Generated product_type_return_rate.png")
else:
    print("No 'productType_X' columns found for product type analysis.")

if 'price' in df.columns:
    fig = px.histogram(df, x='price', color='isReturned',
                      marginal='box', 
                      barmode='overlay',
                      title='Distribution of Price for Returned vs. Non-Returned Items',
                      labels={'price': 'Price', 'isReturned': 'Is Returned'})
    fig.write_image("C:/Users/ADMIN/ET6-CDSP-group-17-repo/3_data_exploration/ASOS_GraphReturns/images/price_distribution.png")
    print("Generated price_distribution.png")
else:
    print("'price' column not found.")

numerical_cols = df.select_dtypes(include=['number']).columns.tolist()
correlation_matrix = df[numerical_cols].corr()
fig = go.Figure(data=go.Heatmap(
                    z=correlation_matrix.values,
                    x=correlation_matrix.columns,
                    y=correlation_matrix.columns,
                    colorscale='Viridis',
                    colorbar=dict(title='Correlation')))
fig.update_layout(
    title='Correlation Matrix of Numerical Features',
    xaxis_tickangle=-45
)
fig.write_image("C:/Users/ADMIN/ET6-CDSP-group-17-repo/3_data_exploration/ASOS_GraphReturns/images/correlation_matrix.png")
print("Generated correlation_matrix.png")