# 📚 Domain Research – Product Return Prediction in E-Commerce

## 🧠 Problem Statement

**Which customer and product-level features are
the strongest predictors of product returns
in e-commerce, and how can optimizing product descriptions
and user experience (UX) reduce these returns?**

---

## 🔍 Research Overview

This project investigates the **systemic causes**
behind high return rates in e-commerce, using **systems thinking** and
the **Iceberg Model**. We explore not only the v
isible return events but also the deeper **patterns**, **structures**,
and **mental models** that contribute to them.

---

## ⛴️ Iceberg Model – Systems Thinking Approach

### 📌 Events

High return rates (15–30%) are common in e-commerce,
especially in fashion (up to 40%).
Returns create major operational and financial challenges.
**Common reasons include:**

* Size or fit issues
* Products not matching descriptions
* Poor product quality or damaged items
* Impulse buying and buyer’s remorse

---

### 📈 Pattern / Trend

* **Fashion and apparel** show highest return rates (20–40%)
* **Electronics and home goods** show 10–20% returns
* **First-time customers** return more than repeat ones
* **Mobile users** return more, often due to poor UX
* **Misleading or incomplete descriptions** increase return probability

---

### 🏗️ Structure

* Lack of **comprehensive product details** (e.g., size, materials)
* Poor **search and filtering** systems
* No **standardized sizing guides**
* Limited **user-generated content** (reviews, photos, Q\&A)
* Weak **mobile UX** makes evaluation difficult
* Absence of **virtual try-on** or AR tools in product view

---

### 💭 Mental Models

* Assumption: "More choices = better experience"
* Overconfidence in fast checkouts over thorough evaluation
* Belief that **return policies replace product accuracy**
* Bias toward blaming customer behavior
* Underestimating **cognitive load** in online buying decisions

---

## 📂 Data Sources

Our project draws on a combination of real-world datasets, academic research,
and industry reports to investigate the causes and predictors of product returns
in e-commerce. Below is an overview of the primary data sources:

---

### 🔢 1. UCI Machine Learning Repository – Online Retail Dataset  

* **Description:** This transactional dataset includes all purchases made between
December 1, 2010 and December 9, 2011 by customers of a UK-based online retailer
that specializes in unique, all-occasion gift items. Many transactions are from
wholesale clients.
***Relevance:** This dataset provides insights into purchasing patterns,
including canceled orders (often used as a proxy for returns).
It allows for analysis of product-level return tendencies in a traditional online
retail context.  
* **Link:** [Online Retail – UCI ML Repo](https://archive.ics.uci.edu/dataset/352/online+retail)

---

### 🌎 2. Kaggle – Brazilian E-Commerce Public Dataset by Olist  

* **Description:** Real commercial data from 100,000 orders placed in Brazil
between 2016 and 2018 across multiple online marketplaces. The dataset covers
customer demographics, product attributes, payment details, freight info, reviews,
and more. A geolocation dataset is also provided.  
* **Relevance:** The dataset enables a multi-dimensional analysis of returns by
  connecting reviews, delivery performance, customer location, and product
  features. Its scale and variety make it especially valuable for building
  predictive models.  
* **Link:** [Brazilian E-Commerce Dataset – Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

---

### 👥 3. Kaggle – Customer Personality Analysis  

* **Description:** This dataset contains detailed demographic, lifestyle,
and purchase behavior data for customers. It includes features such as income,
education level, marital status, and product preferences.  

* **Relevance:** Useful for segmenting customers and exploring how different
customer personas influence the likelihood of returning items. It also helps in
simulating customer-centric strategies for return reduction.  
* **Link:** [Customer Personality Analysis – Kaggle](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)

---

### 📖 4. ACM Digital Library – Research Article  

* **Title:** *Why Do Customers Return Products? Using Customer Reviews to Predict
Product Return Behaviors*  

* **Summary:** This academic paper explores how textual analysis of customer reviews
can reveal the underlying reasons behind returns.
The authors trained a BERT-based classifier that significantly improved
prediction accuracy.  
* **Relevance:** Supports the integration of Natural Language Processing (NLP)
into our project, especially if customer review text becomes part of our dataset
* **Link:** [Read on ACM](https://dl.acm.org/doi/abs/10.1145/3627508.3638326)

---

### 🧾 5. RedHat.com – Article: *Supply Chain Challenges: Handling Returns*  

* **Summary:** Discusses how companies are balancing the need for
customer-friendly return experiences with the costs and risks of excessive returns.
Real-world case examples such as Zappos highlight the operational tradeoffs.  

* **Relevance:** Provides industry context to our problem definition and
potential business recommendations.  
* **Link:** [Read Article](https://www.redhat.com/en/blog/supply-chain-optimization-handling-returns)

---

### 🔄 6. Oracle NetSuite – Article: *13 Reverse Logistics Challenges

* **Summary:** Outlines common challenges faced in reverse logistics, such as
refund processing, waste management, and the environmental footprint of returned
goods.  

* **Relevance:** Highlights logistical and sustainability angles to consider when
modeling or recommending return policies.  
* **Link:** [Read Article](https://www.netsuite.com/portal/resource/articles/inventory-management/reverse-logistics-challenges.shtml)

---

### 📈 7. Supply Chain Dive – Article

* **Summary:** Retailers saw nearly $890 billion in returns in 2023, amounting to
17% of total sales. This article explores return-related fraud and divergent
strategies retailers are using to combat the problem.  

* **Relevance:** Offers up-to-date statistics and shows the real financial scope
of the problem, grounding our research in current events.  
* **Link:** [Read Article](https://www.supplychaindive.com/news/retail-online-returns-reverse-logistics-challenges/737716/)

---

## 💡 Summary

Returns in e-commerce are not just individual events—they reflect deeper patterns
and structural design issues. This project aims to apply
**AI (supervised learning)** to detect return risks early and suggest
design/UX improvements to reduce return rates over time.
