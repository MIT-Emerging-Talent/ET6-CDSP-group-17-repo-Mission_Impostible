import streamlit as st
import pandas as pd
from PIL import Image
import os
BASE_DIR = os.path.dirname(__file__)

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
    [
        "📖 Main Page",
        "🏠 Overview",
        "📦 ASOS Dataset",
        "🛒 TheLook Dataset",
        "📈 Comparison",
        "🚀 Insights to Action"
    ]
)

if selected_dataset == "📖 Main Page":
    st.markdown("## 🛍️ Predicting Product Returns in Fashion E-Commerce")
    st.markdown("""
**Why This Problem Matters**

Fashion e-commerce faces high product return rates, costing businesses billions each year. Returns impact profit, logistics, and customer satisfaction. By predicting which items are likely to be returned, companies can:

- Reduce unnecessary shipping and handling costs
- Improve product listings and sizing guides
- Enhance customer trust and experience
- Make smarter inventory and marketing decisions

Our project explores two different data-driven methods to predict returns, using real-world datasets from leading online retailers.
""")

# Overview Section
elif selected_dataset == "🏠 Overview":
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
    
    # Create tabs for different visualizations, now with Model Performance tab
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Return Patterns", "Customer Analysis", "Product Insights", "Geographic Trends", "Model Performance"
    ])

    with tab1:
        st.markdown("#### Average Discount Value")
        st.image(os.path.join(BASE_DIR,"img", "avgDiscountValue_by_return_status.png"))

        st.markdown("#### Average Gbp Price")
        st.image(os.path.join(BASE_DIR,"img", "avgGbpPrice_by_return_status.png"))

    with tab2:
        st.markdown("#### Return Rates by Age Group")
        st.image(os.path.join(BASE_DIR,"img", "return_rate_by_age.png"))

        st.markdown("#### Customer Return Behavior")
        st.image(os.path.join(BASE_DIR,"img", "return_rate_per_customer.png"))

    with tab3:
        st.markdown("#### Top Product Types by Return Rate")
        st.image(os.path.join(BASE_DIR,"img", "Top10_Product_Types_by_Return_Rate.png"))

        st.markdown("#### Top Brands by Return Rate")
        st.image(os.path.join(BASE_DIR,"img", "Brands_by_Return_Rate.png"))

    with tab4:
        st.markdown("#### Shipping Countries by Return Rate")
        st.image(os.path.join(BASE_DIR,"img", "Top 10 Shipping Countries by Return Rate.png"))

    with tab5:
        st.markdown("### 🎯 Model Performance")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Logistic Regression Results")
            st.image(os.path.join(BASE_DIR,"img", "confusion_matrix_logistic.png"))
            st.image(os.path.join(BASE_DIR,"img", "Feature importance.png"))
        with col2:
            st.markdown("#### Random Forest Results")
            st.image(os.path.join(BASE_DIR, "img", "confusion_matrix_rf.png"))
            st.image(os.path.join(BASE_DIR,"img", "feature_importance_rf.png"))

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
    
    tab1, tab2, tab3, tab4 = st.tabs(["Category Analysis", "Geographic Patterns", "Model Performance", "Model Results"])
    
    with tab1:
        st.markdown("#### Return Rates by Product Category")
        st.image(os.path.join(BASE_DIR, "img", "category.png"))
        
        st.markdown("#### Seasonal Return Patterns")
        st.image(os.path.join(BASE_DIR,"img", "season.png"))
    
    with tab2:
        st.markdown("#### Returns by Country")
        st.image(os.path.join(BASE_DIR,"img", "country.png"))
        
        st.markdown("#### Distribution Center Performance")
        st.image(os.path.join(BASE_DIR, "img", "dc.png"))
    
    with tab3:
        st.markdown("#### Model Comparison", unsafe_allow_html=True)
        st.markdown("""
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Accuracy</th>
      <th>Precision</th>
      <th>Recall</th>
      <th>F1</th>
      <th>ROC-AUC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Logistic</th>
      <td>0.520958</td>
      <td>0.09791</td>
      <td>0.45862</td>
      <td>0.16137</td>
      <td>0.495341</td>
    </tr>
    <tr>
      <th>XGBoost</th>
      <td>0.899505</td>
      <td>0.00000</td>
      <td>0.00000</td>
      <td>0.00000</td>
      <td>0.653133</td>
    </tr>
  </tbody>
</table>
</div>
""", unsafe_allow_html=True)
        
        st.markdown("#### ROC Curves")
        st.image(os.path.join(BASE_DIR, "img", "ROC.png"))
    
    with tab4:
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
    st.markdown(
        """
        <div style="text-align:center; font-size:1.1rem; color:#666; margin-bottom:1rem;">
            Two ways to predict returns. See the differences and pick what fits your need.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Create rich tabs for a clearer experience
    tab_overview, tab_side, tab_perf, tab_when, tab_next = st.tabs([
        "Summary", "Side-by-Side", "Performance", "When to Use", "Next Steps"
    ])

    # 1) SUMMARY TAB
    with tab_overview:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(
                """
                <div class="dataset-card">
                    <h3>📦 ASOS — Graph Method</h3>
                    <p style="margin-top:0.5rem;">Learns patterns from connections between <strong>customers</strong> and <strong>products</strong>.</p>
                    <ul>
                        <li><strong>Best for:</strong> finding hidden relationships, segments</li>
                        <li><strong>Data:</strong> interactions (who bought what)</li>
                        <li><strong>Result:</strong> ~75% accuracy</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                """
                <div class="dataset-card">
                    <h3>🛒 TheLook — Tabular Method</h3>
                    <p style="margin-top:0.5rem;">Treats each purchase as a row with easy-to-read features.</p>
                    <ul>
                        <li><strong>Best for:</strong> quick, explainable decisions</li>
                        <li><strong>Data:</strong> transaction tables</li>
                        <li><strong>Result:</strong> ~65% accuracy</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("### 🎛️ Quick Visual Comparison")
        cc1, cc2 = st.columns(2)
        with cc1:
            st.markdown("**ASOS Accuracy (approx.)**")
            st.progress(75)
        with cc2:
            st.markdown("**TheLook Accuracy (approx.)**")
            st.progress(65)

    # 2) SIDE-BY-SIDE TAB
    with tab_side:
        st.markdown("### ⚖️ Head-to-Head")
        df = pd.DataFrame(
            {
                "Aspect": [
                    "Data Type",
                    "Accuracy",
                    "Interpretability",
                    "Business Use",
                    "Technical Complexity",
                    "Data Requirements",
                ],
                "ASOS (Graph)": [
                    "Customer–Product Network",
                    "~75%",
                    "Moderate (relationships)",
                    "Customer segments, patterns",
                    "High",
                    "Needs interaction links",
                ],
                "TheLook (Tabular)": [
                    "Row-per-Transaction",
                    "~65%",
                    "High (clear features)",
                    "Operations, quick wins",
                    "Low",
                    "Standard tables",
                ],
            }
        )
        st.dataframe(df, use_container_width=True)

        k1, k2 = st.columns(2)
        with k1:
            st.markdown(
                """
                <div class="insight-box" style="color:black;">
                    <h4>Why ASOS wins</h4>
                    <ul>
                        <li>Finds clusters of similar buyers/products</li>
                        <li>Captures "who likes what" patterns</li>
                        <li>Useful for recommendations and targeting</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with k2:
            st.markdown(
                """
                <div class="insight-box" style="color:black;">
                    <h4>Why TheLook wins</h4>
                    <ul>
                        <li>Fast to build and explain</li>
                        <li>Clear feature effects (e.g., category, season)</li>
                        <li>Easier adoption for business teams</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # 3) PERFORMANCE TAB
    with tab_perf:
        st.markdown("### 📊 Model Performance Snapshots")
        p1, p2 = st.columns(2)
        with p1:
            st.markdown("#### ASOS (Graph Models)")
            st.image(os.path.join(BASE_DIR, "img", "confusion_matrix_rf.png"))
            st.image(os.path.join(BASE_DIR, "img", "feature_importance_rf.png"))
        with p2:
            st.markdown("#### TheLook (Tabular Models)")
            st.image(os.path.join(BASE_DIR, "img", "ROC.png"))
            st.markdown(
                """
                <div class="metric-card" style="color:black;">
                    <ul>
                        <li><strong>Logistic Regression:</strong> baseline, easy to interpret</li>
                        <li><strong>XGBoost:</strong> stronger non-linear patterns (ROC-AUC ~0.655)</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # 4) WHEN TO USE TAB
    with tab_when:
        st.markdown("### 🎯 Choose the Right Tool")
        w1, w2 = st.columns(2)
        with w1:
            st.markdown(
                """
                <div class="insight-box" style="color:black;">
                    <h4>Use ASOS (Graph) if you:</h4>
                    <ul>
                        <li>Have rich interaction data</li>
                        <li>Care about relationships and communities</li>
                        <li>Plan recommendations/segment strategies</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with w2:
            st.markdown(
                """
                <div class="insight-box" style="color:black;">
                    <h4>Use TheLook (Tabular) if you:</h4>
                    <ul>
                        <li>Need quick, explainable results</li>
                        <li>Have standard transaction tables</li>
                        <li>Want easy communication with stakeholders</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # 5) NEXT STEPS TAB
    with tab_next:
        st.markdown("### 🚀 Recommended Roadmap")
        st.markdown(
            """
            <div class="dataset-card" style="color:black;">
                <ol>
                    <li><strong>Start Tabular:</strong> deploy a simple model for quick wins</li>
                    <li><strong>Collect Signals:</strong> track interactions (user–product)</li>
                    <li><strong>Add Graphs:</strong> build a graph model for deeper insights</li>
                    <li><strong>Combine:</strong> use both for the best performance and coverage</li>
                </ol>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Insights to Action Section
elif selected_dataset == "🚀 Insights to Action":
    st.markdown("## 🚀 Turning Insights into Action")
    st.markdown("""
Use these findings to drive real business value:

- ✅ **Improve Product Pages:** Use predictions to flag high-return items and add better sizing, photos, or descriptions.
- 📦 **Optimize Logistics:** Preemptively adjust inventory and shipping strategies for likely returns.
- 💬 **Personalize Communication:** Proactively reach out to customers who may need help with fit or product selection.
- 🌍 **Sustainable Practices:** Reduce environmental impact by minimizing unnecessary shipments and returns.
""")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>📊 E-commerce Returns Prediction Analysis | Built with Streamlit</p>
    <p>🎯 Helping businesses understand and reduce product returns through data science</p>
</div>
""", unsafe_allow_html=True)