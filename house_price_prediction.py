# HOUSE PRICE PREDICTION PROJECT

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1.Load Dataset

df = pd.read_csv("house_prices (1).csv")

# Drop unnecessary column
df = df.drop("Property_ID", axis=1)

# One-hot encode categorical variables
df = pd.get_dummies(df, columns=["Location", "Property_Type"], drop_first=True)

# 2️.Prepare Features and Target

X = df.drop("Price", axis=1)
y = df["Price"]

# Train-test split (80-20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Train Models

# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

# Decision Tree
dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)

# Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)


# 4️.Evaluation Function

def evaluate_model(name, y_test, predictions):
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print(f"\n{name} Results")
    print("MAE:", mae)
    print("MSE:", mse)
    print("R2 Score:", r2)


# Evaluate all models
evaluate_model("Linear Regression", y_test, lr_pred)
evaluate_model("Decision Tree", y_test, dt_pred)
evaluate_model("Random Forest", y_test, rf_pred)

# 5️.Predictions vs Actual

# Using Random Forest
plt.figure()
plt.scatter(y_test, rf_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Prices (Random Forest)")

# Save image
plt.savefig("predictions_vs_actual.png")

plt.show(block=False)
plt.pause(3)
plt.close()

# 6️.Feature Importance (Random Forest)

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf.feature_importances_
}).sort_values(by="Importance", ascending=False)

print("\nFeature Importance:")
print(feature_importance)

print("HOUSE PRICE PREDICTION MODEL COMPLETED")
