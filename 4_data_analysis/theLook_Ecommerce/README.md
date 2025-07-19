# TheLook E-commerce Data Analysis

## Overview

This directory contains the comprehensive data analysis and machine learning modeling for the TheLook E-commerce returns prediction project. The analysis focuses on predicting customer returns based on various features including customer behavior, product characteristics, and transaction details.

## 📊 Analysis Workflow

The analysis follows a structured 12-step workflow:

1. **Data Loading** - Reload the prepared feature set from data preparation phase
2. **Feature Engineering** - Minimal encodings and train-test splits
3. **Baseline Modeling** - Logistic Regression as the initial benchmark
4. **Advanced Modeling** - XGBoost for improved performance
5. **Model Evaluation** - Multiple metrics assessment
6. **Feature Importance** - Understanding key predictive signals
7. **Initial Findings** - Summary of baseline results
8. **Exploratory Data Analysis (EDA)** - Deep dive into data patterns
9. **Model Diagnostics** - Error analysis and performance breakdown
10. **Model Robustness** - Cross-validation and learning curves
11. **Advanced Interpretability** - SHAP analysis for model explanations
12. **Business Impact** - Recommendations and next steps

## 🎯 Key Findings

### Model Performance
- **XGBoost outperforms Logistic Regression** on ROC-AUC and F1-score metrics
- **Cross-validation ROC-AUC scores:**
  - Logistic Regression: 0.499 ± 0.003
  - XGBoost: 0.655 ± 0.004
- **Class imbalance:** Approximately 10% return rate in the dataset

### Top Predictive Features
Based on XGBoost feature importance analysis:
1. **Product Category** - Strongest predictor of returns
2. **Distribution Center** - Geographic factors influence returns
3. **Discount Percentage** - Higher discounts correlate with returns
4. **Customer Tenure** - Newer customers more likely to return
5. **Basket Size** - Larger orders show different return patterns

### Error Analysis Insights
- **Highest error rates by category:** Underwear, Plus sizes, Intimates
- **Geographic patterns:** Japan shows highest error rates
- **Basket size impact:** Error rates vary by order size

## 📈 Data Characteristics

### Dataset Overview
- **Size:** 180,952 records with 18 features
- **Target:** Binary return flag (10% positive class)
- **Features:** Mix of categorical and numerical variables

### Key Features Analyzed
- **Customer features:** tenure_days, country, basket_size
- **Product features:** category, brand, season
- **Transaction features:** discount_pct, ship_latency_days
- **Temporal features:** created_dayofweek, created_hour

### Data Quality Issues
- **Missing values** identified in several features:
  - `bin`: 180,952 missing (100%)
  - `ship_latency_days`: 65,911 missing (36%)
  - `tenure_days`: 4,452 missing (2.5%)
  - Other features: season, created_dayofweek, created_hour, brand

## 🔧 Technical Implementation

### Preprocessing Pipeline
- **Numerical features:** Median imputation + Standard scaling
- **Categorical features:** Mode imputation + One-hot encoding
- **Handling unknown categories:** Ignore strategy for new categories

### Model Configuration
- **Logistic Regression:** Balanced class weights, 1000 max iterations
- **XGBoost:** 
  - 300 estimators, learning rate 0.05
  - Max depth 6, subsample 0.8
  - Column sampling 0.8 for regularization

### Evaluation Metrics
- Accuracy, Precision, Recall, F1-score
- ROC-AUC for overall performance
- Confusion matrices for detailed error analysis

## 📊 Visualizations Generated

The analysis produces comprehensive visualizations:
- **Class balance distribution**
- **Feature distributions by return status**
- **Correlation heatmaps**
- **Missing value patterns**
- **ROC and Precision-Recall curves**
- **Confusion matrices (absolute and normalized)**
- **Learning curves**
- **SHAP summary and dependence plots**

## 💼 Business Impact & Recommendations

### Potential Benefits
- **Cost savings** through proactive return management
- **Improved inventory planning** based on return predictions
- **Enhanced customer targeting** strategies
- **Operational efficiency** gains

### Risk Considerations
- **False positives:** Risk of incorrectly flagging non-returning customers
- **False negatives:** Missing likely returns increases operational costs
- **Model drift:** Performance may degrade over time

### Model Improvement

1. **Model Optimization**
   - Implement hyperparameter tuning for XGBoost
   - Optimize probability thresholds for business objectives
   - Consider ensemble methods for improved robustness

2. **Deployment Strategy**
   - Deploy with continuous monitoring
   - Implement A/B testing for model impact
   - Set up automated retraining pipelines

3. **Continuous Improvement**
   - Collect feedback on model predictions
   - Monitor new data patterns
   - Iterate on feature engineering
   - Regular model performance reviews

## 📁 Files

- `theLookdata_analysis.ipynb` - Complete analysis notebook with all code, visualizations, and findings

## 🔗 Dependencies

The analysis requires the following Python packages:
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- xgboost
- shap

## 📝 Notes

- The analysis uses stratified sampling to maintain class balance
- All models are evaluated using cross-validation for robustness
- SHAP analysis provides interpretable explanations for business users
- The workflow is designed to be reproducible and extensible 