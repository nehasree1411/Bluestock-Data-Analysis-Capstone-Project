# BlueStock Mutual Fund Analytics Capstone
## 🚀 Project Overview

This project is an end-to-end Mutual Fund Analytics System that covers:

1. Data ingestion & cleaning (ETL pipeline)
2. SQL database design (SQLite)
3. Exploratory Data Analysis (EDA)
4. Financial performance metrics
5. Advanced analytics (VaR, CVaR, Monte Carlo)
6. Recommendation system
7. Interactive Power BI dashboard

The goal is to transform raw mutual fund datasets into actionable insights for investors.

## 📁 Project Structure
BlueStock_Project/

│
├── Data/
│   ├── Raw/                 
│   ├── Processed/
│   └── bluestock_mf.sql
│
├── Notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── Scripts/
│   ├── etl_pipeline.ipynb
│   ├── live_nav_fetch.py
│   └── recommender.py
│
├── SQL/
│   ├── schema.sql
│   └── queries.sql
│
├── Dashboard/
│   ├── bluestock_mf_dashboard.pbix
│   ├── Dashboard.pdf
│   └── monte_carlo_simulation.png
│
├── Reports/
│   └── data_dictionary.md
│
└── requirements.txt

## ⚙️ Tech Stack
Python: pandas, numpy, matplotlib, seaborn, plotly
SQL: SQLite
Visualization: Power BI
Analytics: Financial modeling, risk metrics
Tools: Jupyter Notebook, VS Code

## 🔄 ETL Pipeline
Extracted 10 raw datasets
Cleaned missing values, data types, inconsistencies
Created structured datasets in /Processed
Loaded into SQLite database

## 📊 Key Analyses

1. Exploratory Data Analysis (EDA)
AUM trends across fund houses
SIP inflows over time
Category-wise investment distribution
Benchmark comparisons

2. Performance Metrics
Calculated:
Returns (1Y, 3Y, 5Y)
Sharpe Ratio
Alpha & Beta
Volatility

Output files:
alpha_beta.csv
fund_scorecard.csv

3. Risk Analytics
Value at Risk (VaR)
Conditional VaR (CVaR)

Output:
var_cvar_report.csv

4. Recommender System
Suggests funds based on:
Risk level
Performance
Category

## 🗄️ Database Design
Star schema implemented
Fact + Dimension tables
SQL queries for:
Top funds by AUM
Risk-return analysis
Category trends

## 📈 Dashboard (Power BI)

#### Dashboard includes:

KPI Cards (AUM, Returns, Risk)
Fund comparison visuals
Category-wise analysis
Time-series trends
Interactive slicers

File:
Dashboard/bluestock_mf_dashboard.pbix

## ▶️ How to Run
1. Install dependencies
pip install -r requirements.txt
2. Run notebooks
Open in Jupyter:
Notebooks/
3. Run scripts
python Scripts/live_nav_fetch.py
python Scripts/recommender.py
4. Open Dashboard
Open .pbix file in Power BI Desktop

## 📌 Key Outcomes
Built complete data pipeline
Designed financial analytics system
Implemented risk modeling (VaR, CVaR)
Created interactive BI dashboard
Developed fund recommendation engine

## 🧠 Learnings
End-to-end data science workflow
Financial analytics & portfolio theory
SQL schema design
Dashboard storytelling
Real-world data challenges

## 📎 Deliverables Mapping
Deliverable	Status
ETL Pipeline	✅ Completed
SQLite DB	✅ Completed
EDA	✅ Completed
Performance Metrics	✅ Completed
Dashboard	✅ Completed
Advanced Analytics	✅ Completed
Final Report	✅ Completed

## 👤 Author
Nehasree Uma Tadikonda
BSc (Hons) – IIT Guwahati

## ⭐ Notes
This is a capstone-level project demonstrating:
1. Data engineering
2. Data analysis
3. Financial modeling
4. Business intelligence
