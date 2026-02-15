#churn_prediction_pipeline
# Day 1 - Data Exploration

import pandas as pd
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

import warnings
warnings.filterwarnings("ignore")
# Load dataset
df = pd.read_csv("customer_churn.csv")

# Drop ID column if exists
if 'CustomerID' in df.columns:
    df.drop('CustomerID', axis=1, inplace=True)

# Basic inspection
print(df.head())
print(df.shape)

# Data types
print(df.info())

# Statistical summary
print(df.describe())

# Missing values
print(df.isnull().sum())

# Churn distribution
print(df['Churn'].value_counts())
print(df['Churn'].value_counts(normalize=True))

# Day 2 - Encoding


# Copy dataframe
df2 = df.copy()

# 1️.Label Encoding (Binary Columns)
le = LabelEncoder()

binary_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'Churn']

for col in binary_cols:
    if col in df2.columns:
        df2[col] = le.fit_transform(df2[col])

# 2️. One-Hot Encoding (Nominal Columns)
nominal_cols = ['InternetService', 'PaymentMethod']

df2 = pd.get_dummies(df2, columns=[col for col in nominal_cols if col in df2.columns], drop_first=True)

# 3. Ordinal Encoding (Ordered categories)
ordinal_cols = ['Contract']

if 'Contract' in df2.columns:
    oe = OrdinalEncoder()
    df2[['Contract']] = oe.fit_transform(df2[['Contract']])

print(df2.head())

# Day 3 - Scaling


df3 = df2.copy()

# Numerical columns
num_cols = df3.select_dtypes(include=np.number).columns.tolist()
num_cols.remove('Churn')  # target variable

# 1️.Min-Max Scaling
mms = MinMaxScaler()
df3[num_cols] = mms.fit_transform(df3[num_cols])

# 2️. Standard Scaling (for comparison)
scaler = StandardScaler()
df_standard = df2.copy()
df_standard[num_cols] = scaler.fit_transform(df_standard[num_cols])

print(df3.head())
print(df_standard.head())

# Day 4 - Outlier Handling

df4 = df3.copy()

# 1️. IQR Method
Q1 = df4['MonthlyCharges'].quantile(0.25)
Q3 = df4['MonthlyCharges'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df4 = df4[(df4['MonthlyCharges'] >= lower) &
          (df4['MonthlyCharges'] <= upper)]

# 2️. Z-Score Method

z_scores = np.abs(stats.zscore(df4[num_cols]))
df4 = df4[(z_scores < 3).all(axis=1)]

print(df4.shape)

# Day 5 - Feature Engineering

df5 = df4.copy()

# 1️. Customer Lifetime Value
df5['CLV'] = df5['MonthlyCharges'] * df5['Tenure']

# 2️. Average Monthly Spend
if 'TotalCharges' in df5.columns:
    df5['AvgMonthlySpend'] = df5['TotalCharges'] / (df5['Tenure'] + 1)

# 3️. Tenure Group
df5['TenureGroup'] = pd.cut(df5['Tenure'],
                            bins=[0,12,24,48,72],
                            labels=[1,2,3,4])

# 4️. Charges Per Year
df5['ChargesPerYear'] = df5['MonthlyCharges'] * 12

# 5️. High Value Customer Flag
df5['HighValueCustomer'] = np.where(df5['MonthlyCharges'] > df5['MonthlyCharges'].median(), 1, 0)

print(df5.head())

# Day 6 - Feature Selection


df6 = df5.copy()

# Correlation Matrix
plt.figure(figsize=(10,8))
sns.heatmap(df6.corr(), cmap='coolwarm')
plt.show()

# Split features & target
X = df6.drop('Churn', axis=1)
y = df6['Churn']

# Random Forest Feature Importance
model = RandomForestClassifier()
model.fit(X, y)

importance = pd.Series(model.feature_importances_, index=X.columns)
importance = importance.sort_values(ascending=False)

print(importance.head(10))

# Day 7 - Complete Pipeline

# Reload original data for clean pipeline
df_pipeline = pd.read_csv("customer_churn.csv")

# Define features and target
X = df_pipeline.drop('Churn', axis=1)
y = df_pipeline['Churn']

# Identify column types
num_cols = X.select_dtypes(include=np.number).columns
cat_cols = X.select_dtypes(include='object').columns

# Pipelines
numeric_pipeline = Pipeline([
    ('scaler', StandardScaler())
])

categorical_pipeline = Pipeline([
    ('onehot', OneHotEncoder(drop='first', handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('num', numeric_pipeline, num_cols),
    ('cat', categorical_pipeline, cat_cols)
])

final_pipeline = Pipeline([
    ('preprocessing', preprocessor),
    ('model', RandomForestClassifier())
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
final_pipeline.fit(X_train, y_train)

# Predict
y_pred = final_pipeline.predict(X_test)

print(classification_report(y_test, y_pred))
