# Task 8
# Customer Churn Business Analysis Project

## Project Overview
This project presents a complete end-to-end business analysis focused on understanding customer behavior and churn patterns. The objective is to analyze customer data, identify key factors influencing churn, and provide data-driven recommendations with a clear business implementation plan.

The project follows a structured analytics workflow including data collection, data cleaning, exploratory data analysis (EDA), advanced statistical analysis, visualization, and insight generation using Python.

---

## Objectives
- Analyze customer churn behavior using real business data
- Perform data cleaning and preprocessing for accurate analysis
- Conduct exploratory and statistical analysis
- Create professional visualizations for business interpretation
- Generate actionable insights and recommendations for decision-making

---

## Dataset
The dataset used in this project is:

**customer_churn.csv**

### Dataset Details
- Rows: 500+
- Type: Structured business data

### Columns:
- **Tenure** – Length of customer relationship
- **MonthlyCharges** – Monthly charges paid by the customer
- **TotalCharges** – Total amount billed
- **Contract** – Contract type
- **PaymentMethod** – Mode of payment
- **PaperlessBilling** – Paperless billing status
- **SeniorCitizen** – Senior citizen indicator
- **Churn** – Customer churn status (Yes / No)

---

## Project Structure
├── data/
│ ├── raw_data.csv
│ └── cleaned_data.csv
├── notebooks/
│ ├── 1_data_cleaning.ipynb
│ ├── 2_eda.ipynb
│ └── 3_analysis.ipynb
├── reports/
│ ├── executive_summary.pdf
│ └── technical_report.pdf
├── presentations/
│ └── business_presentation.pptx
├── requirements.txt
└── README.md

---

## Analysis Workflow

### Phase 1: Data Cleaning
- Verified dataset structure and quality
- Checked and confirmed absence of missing values
- Encoded categorical variables for analysis
- Saved cleaned data for reuse

Notebook: `notebooks/1_data_cleaning.ipynb`

---

### Phase 2: Exploratory Data Analysis (EDA)
- Distribution analysis of numerical variables
- Comparative analysis of churned vs non-churned customers
- Correlation analysis using heatmaps
- Identification of patterns affecting churn

Notebook: `notebooks/2_eda.ipynb`

---

### Phase 3: Advanced Analysis
- Statistical analysis of customer segments
- Validation of business assumptions
- Interpretation of analytical results

Notebook: `notebooks/3_analysis.ipynb`

---

## Visualizations
The project includes more than five professional visualizations:
- Histograms for charges distribution
- Bar charts for churn comparison
- Correlation heatmaps
- Categorical analysis plots
- Trend-based visual representations

All visualizations were generated using **matplotlib** and **seaborn**.

---

## Tools and Technologies
- Python
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- Jupyter Notebook

---

## Key Insights
- Customers with higher monthly charges are more likely to churn
- Contract type has a strong impact on customer retention
- Long-tenure customers show lower churn probability
- Billing and payment methods influence customer behavior

---

## Business Recommendations
- Introduce retention offers for high monthly charge customers
- Encourage customers to opt for long-term contracts
- Improve customer engagement for new customers
- Optimize payment and billing options to enhance retention

---

## Setup Instructions
1. Clone or download the project repository
2. Install required dependencies:
3. Run notebooks in the following order:
- `1_data_cleaning.ipynb`
- `2_eda.ipynb`
- `3_analysis.ipynb`

---

## Quality Standards Checklist
- End-to-end business analysis completed
- Dataset size meets internship requirements
- Multiple analysis techniques applied
- Professional visualizations included
- Complete documentation provided
- Business insights and implementation plan included

---

## Author
**Ishika Ambagade**  
Final Year Engineering Student  
Business Analytics Internship Project




















