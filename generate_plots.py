
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Create a directory for the images if it doesn't exist
output_dir = "C:/Users/ADMIN/ET6-CDSP-group-17-repo/3_data_exploration/ASOS_GraphReturns/images"
os.makedirs(output_dir, exist_ok=True)

# Load the prepared data
prepared_data_path = 'C:/Users/ADMIN/ET6-CDSP-group-17-repo/2_data_preparation/ASOS_GraphReturns/prepared_asos_data.csv'
df = pd.read_csv(prepared_data_path)

# --- 1. Overall Return Share ---
return_counts = df['isReturned'].value_counts()
fig1 = px.pie(names=['Not Returned (0)', 'Returned (1)'], 
             values=return_counts.values,
             title='Overall Product Return Distribution',
             hole=0.3)
fig1.update_traces(textinfo='percent+label', pull=[0, 0.1])
fig1.write_image(os.path.join(output_dir, "return_distribution.png"))

# --- 2. Return Rate by Gender ---
if 'isMale' in df.columns:
    gender_return_rate = df.groupby('isMale')['isReturned'].mean().reset_index()
    gender_return_rate['isMale'] = gender_return_rate['isMale'].map({0: 'Female', 1: 'Male'})
    fig2 = px.bar(gender_return_rate, x='isMale', y='isReturned',
                 title='Return Rate by Gender',
                 labels={'isMale': 'Gender', 'isReturned': 'Average Return Rate'},
                 text=gender_return_rate['isReturned'].apply(lambda x: f'{x:.2%}'))
    fig2.write_image(os.path.join(output_dir, "gender_return_rate.png"))

# --- 3. Return Rate by Shipping Country (Top 10) ---
country_cols = [col for col in df.columns if col.startswith('Country_') and col != 'Country_Other']
if country_cols:
    country_return_rates = {col.replace('Country_', ''): df[df[col] == 1]['isReturned'].mean() for col in country_cols}
    country_return_rates_series = pd.Series(country_return_rates).sort_values(ascending=False).head(10)
    fig3 = px.bar(x=country_return_rates_series.index, y=country_return_rates_series.values,
                 title='Return Rate by Top 10 Shipping Countries',
                 labels={'x': 'Country', 'y': 'Average Return Rate'},
                 text=country_return_rates_series.values)
    fig3.update_traces(texttemplate='%{text:.2%}', textposition='outside')
    fig3.update_layout(xaxis_tickangle=-45)
    fig3.write_image(os.path.join(output_dir, "country_return_rate.png"))

# --- 4. Return Rate by Product Type (Top 10) ---
product_type_cols = [col for col in df.columns if col.startswith('productType_') and col != 'productType_Other']
if product_type_cols:
    product_type_return_rates = {col.replace('productType_', ''): df[df[col] == 1]['isReturned'].mean() for col in product_type_cols}
    product_type_return_rates_series = pd.Series(product_type_return_rates).sort_values(ascending=False).head(10)
    fig4 = px.bar(x=product_type_return_rates_series.index, y=product_type_return_rates_series.values,
                 title='Return Rate by Top 10 Product Types',
                 labels={'x': 'Product Type', 'y': 'Average Return Rate'},
                 text=product_type_return_rates_series.values)
    fig4.update_traces(texttemplate='%{text:.2%}', textposition='outside')
    fig4.update_layout(xaxis_tickangle=-45)
    fig4.write_image(os.path.join(output_dir, "product_type_return_rate.png"))

# --- 5. Price Distribution ---
if 'price' in df.columns:
    fig5 = px.histogram(df, x='price', color='isReturned',
                      marginal='box', 
                      barmode='overlay',
                      title='Distribution of Price for Returned vs. Non-Returned Items',
                      labels={'price': 'Price', 'isReturned': 'Is Returned'})
    fig5.write_image(os.path.join(output_dir, "price_distribution.png"))

# --- 6. Correlation Matrix ---
numerical_cols = df.select_dtypes(include=['number']).columns.tolist()
correlation_matrix = df[numerical_cols].corr()
fig6 = go.Figure(data=go.Heatmap(
                    z=correlation_matrix.values,
                    x=correlation_matrix.columns,
                    y=correlation_matrix.columns,
                    colorscale='Viridis',
                    colorbar=dict(title='Correlation')))
fig6.update_layout(
    title='Correlation Matrix of Numerical Features',
    xaxis_tickangle=-45
)
fig6.write_image(os.path.join(output_dir, "correlation_matrix.png"))

print("Successfully generated and saved all plots.")
