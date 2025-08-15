import streamlit as st
import pandas as pd
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="E-commerce Returns Prediction",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .dataset-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    .insight-box {
        background: #e8f4fd;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #bee5eb;
        margin: 1rem 0;
    }
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">🛍️ E-commerce Returns Prediction</h1>', unsafe_allow_html=True)

# Introduction section
st.markdown("""
<div style="text-align: center; font-size: 1.2rem; color: #666; margin-bottom: 3rem;">
    Understanding why customers return products helps businesses improve customer satisfaction and reduce costs.
    <br>We analyzed two different approaches to predict returns using real e-commerce data.
</div>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("📊 Navigation")
selected_dataset = st.sidebar.radio(
    "Choose a dataset to explore:",
    ["🏠 Overview", "📦 ASOS Dataset", "🛒 TheLook Dataset", "📈 Comparison"]
)

# Overview Section
if selected_dataset == "🏠 Overview":
    st.markdown("## 🎯 Project Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="metric-card" style="color:black;">
            <h3>🧠 What We're Solving</h3>
            <p>Product returns cost e-commerce businesses billions annually. By predicting which items are likely to be returned, companies can:</p>
            <ul>
                <li>Improve product descriptions and sizing</li>
                <li>Optimize inventory management</li>
                <li>Enhance customer experience</li>
                <li>Reduce operational costs</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card" style="color:black;">
            <h3>🔬 Our Approach</h3>
            <p>We tested two different methods to predict returns:</p>
            <ul>
                <li><strong>Traditional Method:</strong> Analyzing individual purchases</li>
                <li><strong>Graph Method:</strong> Understanding customer-product relationships</li>
            </ul>
            <p>Each method has unique strengths for different business scenarios.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("## 📊 Quick Results")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("ASOS Accuracy", "75%", "Good")
    
    with col2:
        st.metric("TheLook Accuracy", "65%", "Moderate")
    
    with col3:
        st.metric("Total Records", "180K+", "Large Dataset")
    
    with col4:
        st.metric("Return Rate", "10%", "Industry Average")

# ASOS Dataset Section
elif selected_dataset == "📦 ASOS Dataset":
    st.markdown("## 📦 ASOS Dataset Analysis")
    
    st.markdown("""
    <div class="dataset-card">
        <h2>🧩 Graph-Based Approach</h2>
        <p>The ASOS dataset uses a network approach where customers and products are connected through purchases. 
        This helps us understand patterns like "customers who return certain products often return similar items."</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key findings
    st.markdown("### 🔍 Key Discoveries")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="insight-box" style="color:black;">
            <h4>👥 Customer Behavior</h4>
            <ul>
                <li>Most customers return products only once or twice</li>
                <li>A small group of customers are frequent returners</li>
                <li>Past return behavior strongly predicts future returns</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-box" style="color:black;">
            <h4>🛍️ Product Patterns</h4>
            <ul>
                <li>Certain product types have consistently higher return rates</li>
                <li>Brand reputation affects return likelihood</li>
                <li>Geographic location influences return behavior</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Visualizations section
    st.markdown("### 📊 Data Visualizations")
    
    # Create tabs for different visualizations
    tab1, tab2, tab3, tab4 = st.tabs(["Return Patterns", "Customer Analysis", "Product Insights", "Geographic Trends"])
    
    with tab1:
        st.markdown("#### Return Frequency Distribution")
        st.markdown('<img src="return_frequency.png">', unsafe_allow_html=True)
        
        st.markdown("#### Return Rate Distribution")
        st.markdown('<img src="return_rate_distribution.png">', unsafe_allow_html=True)
    
    with tab2:
        st.markdown("#### Return Rates by Age Group")
        st.markdown('<img src="return_rate_by_age_group.png">', unsafe_allow_html=True)
        
        st.markdown("#### Customer Return Behavior")
        st.markdown('<img src="customer_behavior_analysis.png">', unsafe_allow_html=True)
    
    with tab3:
        st.markdown("#### Top Product Types by Return Rate")
        st.markdown('<img src="Top 10 Product Types by Return Rate.png">', unsafe_allow_html=True)
        
        st.markdown("#### Top Brands by Return Rate")
        st.markdown('<img src="Top 10 Brands by Return Rate.png">', unsafe_allow_html=True)
    
    with tab4:
        st.markdown("#### Shipping Countries by Return Rate")
        st.markdown('<img src="Top 10 Shipping Countries by Return Rate.png">', unsafe_allow_html=True)
    
    # Model Performance
    st.markdown("### 🎯 Model Performance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Logistic Regression Results")
        st.markdown('<img src="confusion_matrix_logistic.png">', unsafe_allow_html=True)
        st.markdown('<img src="feature_importance_logistic.png">', unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### Random Forest Results")
        st.markdown('<img src="confusion_matrix_rf.png">', unsafe_allow_html=True)
        st.markdown('<img src="feature_importance_rf.png">', unsafe_allow_html=True)

# TheLook Dataset Section
elif selected_dataset == "🛒 TheLook Dataset":
    st.markdown("## 🛒 TheLook E-commerce Dataset")
    
    st.markdown("""
    <div class="dataset-card">
        <h2>📊 Traditional Tabular Approach</h2>
        <p>The TheLook dataset treats each purchase as an individual record with features like customer age, 
        product category, price, and shipping details. This is the most common approach in e-commerce analytics.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Dataset overview
    st.markdown("### 📋 Dataset Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Records", "180,952", "Large Scale")
    
    with col2:
        st.metric("Return Rate", "10%", "Balanced")
    
    with col3:
        st.metric("Features", "18", "Rich Data")
    
    # Key insights
    st.markdown("### 🔍 Key Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="insight-box" style="color:black;">
            <h4>🎯 What Affects Returns</h4>
            <ul>
                <li><strong>Product Category:</strong> Clothing sets have highest return rates (11.9%)</li>
                <li><strong>Season:</strong> Fall season shows higher returns</li>
                <li><strong>Geography:</strong> Germany and Australia lead in returns</li>
                <li><strong>Discounts:</strong> Discounted items have different return patterns</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-box" style="color:black;">
            <h4>🤔 Surprising Findings</h4>
            <ul>
                <li><strong>Gender:</strong> Almost no difference between male/female returns</li>
                <li><strong>Age:</strong> Minimal impact on return behavior</li>
                <li><strong>Price:</strong> Not a strong predictor of returns</li>
                <li><strong>Shipping Time:</strong> Less important than expected</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Visualizations
    st.markdown("### 📊 Data Visualizations")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Category Analysis", "Geographic Patterns", "Model Performance", "Feature Importance"])
    
    with tab1:
        st.markdown("#### Return Rates by Product Category")
        st.markdown('<img src="category_return_rates.png">', unsafe_allow_html=True)
        
        st.markdown("#### Seasonal Return Patterns")
        st.markdown('<img src="seasonal_patterns.png">', unsafe_allow_html=True)
    
    with tab2:
        st.markdown("#### Returns by Country")
        st.markdown('<img src="geographic_returns.png">', unsafe_allow_html=True)
        
        st.markdown("#### Distribution Center Performance")
        st.markdown('<img src="distribution_center_analysis.png">', unsafe_allow_html=True)
    
    with tab3:
        st.markdown("#### Model Comparison")
        st.markdown('<img src="model_comparison.png">', unsafe_allow_html=True)
        
        st.markdown("#### ROC Curves")
        st.markdown('<img src="roc_curves.png">', unsafe_allow_html=True)
    
    with tab4:
        st.markdown("#### XGBoost Feature Importance")
        st.markdown('<img src="xgboost_feature_importance.png">', unsafe_allow_html=True)
        
        st.markdown("#### SHAP Analysis")
        st.markdown('<img src="shap_analysis.png">', unsafe_allow_html=True)
    
    # Model Results
    st.markdown("### 🎯 Model Results")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="metric-card" style="color:black;">
            <h4>📈 Logistic Regression</h4>
            <ul>
                <li><strong>Accuracy:</strong> Baseline performance</li>
                <li><strong>Pros:</strong> Easy to interpret, fast training</li>
                <li><strong>Cons:</strong> Limited pattern recognition</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card" style="color:black;">
            <h4>🚀 XGBoost</h4>
            <ul>
                <li><strong>ROC-AUC:</strong> 0.655 (65.5% accuracy)</li>
                <li><strong>Pros:</strong> Better pattern recognition</li>
                <li><strong>Cons:</strong> More complex, harder to interpret</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Comparison Section
elif selected_dataset == "📈 Comparison":
    st.markdown("## 📈 Method Comparison")
    
    st.markdown("""
    <div style="text-align: center; font-size: 1.1rem; color: #666; margin-bottom: 2rem;">
        Both approaches offer unique insights into e-commerce returns. Here's how they compare:
    </div>
    """)
    
    # Comparison table
    st.markdown("### ⚖️ Head-to-Head Comparison")
    
    comparison_data = {
        "Aspect": ["Data Type", "Accuracy", "Interpretability", "Business Use", "Technical Complexity", "Data Requirements"],
        "ASOS (Graph Method)": [
            "Customer-Product Networks", 
            "75% (Good)", 
            "Moderate - Shows relationships", 
            "Understanding customer segments", 
            "High - Requires graph expertise", 
            "Needs relationship data"
        ],
        "TheLook (Traditional Method)": [
            "Individual Transactions", 
            "65% (Moderate)", 
            "High - Clear feature impact", 
            "Operational decisions", 
            "Low - Standard ML approach", 
            "Standard transaction data"
        ]
    }
    
    comparison_df = pd.DataFrame(comparison_data)
    st.table(comparison_df)
    
    # When to use each method
    st.markdown("### 🎯 When to Use Each Method")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="insight-box" style="color:black;">
            <h4>📦 Use ASOS Method When:</h4>
            <ul>
                <li>You have rich customer-product interaction data</li>
                <li>You want to understand customer segments</li>
                <li>You're building recommendation systems</li>
                <li>You have technical expertise in graph analysis</li>
                <li>You want to find hidden patterns in behavior</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-box" style="color:black;">
            <h4>🛒 Use TheLook Method When:</h4>
            <ul>
                <li>You need quick, interpretable results</li>
                <li>You're making operational decisions</li>
                <li>You have standard transaction data</li>
                <li>You need to explain results to stakeholders</li>
                <li>You're starting with basic analytics</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Business recommendations
    st.markdown("### 💼 Business Recommendations")
    
    st.markdown("""
    <div class="dataset-card" style="color:black;">
        <h3>🚀 Best Practice Approach</h3>
        <p><strong>Start with TheLook method</strong> for immediate insights and operational improvements. 
        <strong>Evolve to ASOS method</strong> as you collect more data and build technical capabilities.</p>
        
        <h4>Implementation Roadmap:</h4>
        <ol>
            <li><strong>Phase 1:</strong> Implement basic return prediction with transaction data</li>
            <li><strong>Phase 2:</strong> Collect customer behavior and interaction data</li>
            <li><strong>Phase 3:</strong> Build graph-based models for deeper insights</li>
            <li><strong>Phase 4:</strong> Combine both approaches for maximum effectiveness</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # Final insights
    st.markdown("### 🎯 Key Takeaways")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card" style="color:black;">
            <h4>🔍 For Analysis</h4>
            <p>Both methods reveal that product category and customer history are the strongest predictors of returns.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card" style="color:black;">
            <h4>💡 For Business</h4>
            <p>Focus on improving product descriptions, sizing guides, and customer education rather than demographic targeting.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card" style="color:black;">
            <h4>🚀 For Future</h4>
            <p>Combine both approaches with real-time data for dynamic return prediction and prevention strategies.</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>📊 E-commerce Returns Prediction Analysis | Built with Streamlit</p>
    <p>🎯 Helping businesses understand and reduce product returns through data science</p>
</div>
""", unsafe_allow_html=True)