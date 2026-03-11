import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle

#Load dataset
df=pd.read_csv("customer_churn.csv")

#basic inspection
print(df.head())
print(df.shape)
print(df.columns)
#data types
df.info()

#missing value
print(df.isnull().sum())

print(df["Churn"].value_counts())
print(df.select_dtypes(include="object").columns)

# Churn distribution plot/count plot
sns.countplot(x="Churn", data=df)

plt.title("Churn Distribution")
plt.xlabel("Churn (0 = Stayed, 1 = Left)")
plt.ylabel("Number of Customers")

plt.show()

#Contract vs Churn/count plot
plt.figure(figsize=(6,4))

sns.countplot(x="Contract", hue="Churn", data=df)

plt.title("Contract Type vs Churn")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")

plt.show()

#Payment Method vs Churn
plt.figure(figsize=(6,4))

sns.countplot(x="PaymentMethod", hue="Churn", data=df)

plt.title("Payment Method vs Churn")
plt.xlabel("Payment Method")
plt.ylabel("Number of Customers")

plt.xticks(rotation=45)

plt.show()

#Paperless Billing vs Churn/count plot
plt.figure(figsize=(6,4))

sns.countplot(x="PaperlessBilling", hue="Churn", data=df)

plt.title("Paperless Billing vs Churn")
plt.xlabel("Paperless Billing")
plt.ylabel("Number of Customers")

plt.show()

#drop customerID
df = df.drop("CustomerID", axis=1)

#Convert categorical columns into numbers
df = pd.get_dummies(df, columns=["PaperlessBilling","PaymentMethod","Contract"], drop_first=True)

#Separate features and target
X=df.drop("Churn",axis=1)
y=df["Churn"]

#split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#Train models

#model=Logistic regression
model = LogisticRegression(max_iter=1000)

#train the model
model.fit(X_train,y_train)

#make predictions
y_pred=model.predict(X_test)

#Evaluate the Model
print("Accuracy:",accuracy_score(y_test,y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test,y_pred))

print("Classification Report:")
print(classification_report(y_test,y_pred))

#model=decision tree classifier
model=DecisionTreeClassifier()

#train
model.fit(X_train,y_train)

#make predictions
y_pred=model.predict(X_test)

#evaluate
print("Accuracy",accuracy_score(y_test,y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test,y_pred))

print("Classification Report:")
print(classification_report(y_test,y_pred))

#model=random forest
# model = Random Forest
model = RandomForestClassifier()

#train
model.fit(X_train, y_train)

#make predictions
y_pred = model.predict(X_test)

#evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save trained model
with open("churn_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")
