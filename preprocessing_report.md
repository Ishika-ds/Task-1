# Customer Churn Prediction – Preprocessing Report

## 1. Dataset Overview

The dataset contains 500 customer records with 8 original features:

- Tenure
- MonthlyCharges
- TotalCharges
- Contract
- PaymentMethod
- PaperlessBilling
- SeniorCitizen
- Churn (Target Variable)

### Dataset Characteristics:
- Total Records: 500
- No missing values detected
- 3 categorical features
- 5 numerical features
- Churn distribution:
  - Non-Churn: 89.4%
  - Churn: 10.6%

The dataset shows class imbalance, with churn customers representing a minority class.

---

## 2. Handling Categorical Data

Three encoding methods were implemented:

### 2.1 Label Encoding
Used for binary categorical variables such as:
- PaperlessBilling
- Churn

Converted categories into numerical format (0 and 1).

### 2.2 One-Hot Encoding
Applied to nominal variables:
- PaymentMethod

This prevents introducing ordinal relationships between categories.

### 2.3 Ordinal Encoding
Applied to:
- Contract

Since contract types can represent an ordered structure (e.g., month-to-month vs long-term).

---

## 3. Feature Scaling

Two scaling techniques were implemented:

### 3.1 Min-Max Scaling
Formula:
X' = (X - Xmin) / (Xmax - Xmin)

Scaled features to the range [0,1].

### 3.2 Standard Scaling
Formula:
Z = (X - μ) / σ

Centered data with mean = 0 and standard deviation = 1.

Comparison was performed to observe distribution changes after scaling.

---

## 4. Outlier Detection and Handling

Two methods were used:

### 4.1 IQR Method
IQR = Q3 - Q1  
Outliers were removed outside:

Lower Bound = Q1 - 1.5 × IQR  
Upper Bound = Q3 + 1.5 × IQR  

Applied primarily to MonthlyCharges.

### 4.2 Z-Score Method
Z = (X - μ) / σ  

Observations with Z-score > 3 were removed.

---

## 5. Feature Selection

Feature selection was performed using:

### 5.1 Correlation Analysis
A heatmap was generated using only numerical features to identify strong relationships.

### 5.2 Random Forest Feature Importance
Feature importance ranking showed:

- Tenure (most important)
- CLV
- AvgMonthlySpend
- Contract

This confirms business logic: long-term and high-value customers are less likely to churn.

---

## 6. Data Pipeline Implementation

A complete preprocessing pipeline was built using:

- ColumnTransformer
- StandardScaler
- OneHotEncoder
- RandomForestClassifier

The pipeline ensures:
- No data leakage
- Automated preprocessing
- End-to-end reproducibility

---

## 7. Observations

- Dataset is imbalanced.
- Tenure is the strongest predictor of churn.
- Feature engineering significantly improved model interpretability.
- Class imbalance affected recall for churn prediction.

---

## Conclusion

Comprehensive preprocessing improved model performance and ensured clean, structured data transformation suitable for machine learning.
