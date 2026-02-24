import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

df = pd.read_csv("customer_churn.csv")
df = df.dropna()

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype('category').cat.codes

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df.drop("Churn", axis=1))

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

kmeans = KMeans(n_clusters=3, random_state=42)
df["KMeans_Segment"] = kmeans.fit_predict(X_scaled)

agg = AgglomerativeClustering(n_clusters=3)
df["Hierarchical_Segment"] = agg.fit_predict(X_scaled)

dbscan = DBSCAN(eps=0.5, min_samples=5)
df["DBSCAN_Segment"] = dbscan.fit_predict(X_scaled)

results = []

for segment in df["KMeans_Segment"].unique():
    segment_df = df[df["KMeans_Segment"] == segment]

    if len(segment_df) < 10:
        continue

    X = segment_df.drop(
        ["Churn", "KMeans_Segment", "Hierarchical_Segment", "DBSCAN_Segment"],
        axis=1
    )
    y = segment_df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    rf = RandomForestClassifier(random_state=42)

    param_grid = {
        "n_estimators": [50, 100],
        "max_depth": [None, 5, 10]
    }

    grid = GridSearchCV(rf, param_grid, cv=3)
    grid.fit(X_train, y_train)

    best_model = grid.best_estimator_

    y_pred = best_model.predict(X_test)
    y_prob = best_model.predict_proba(X_test)[:, 1]

    results.append({
        "Segment": segment,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1": f1_score(y_test, y_pred),
        "ROC_AUC": roc_auc_score(y_test, y_prob)
    })

results_df = pd.DataFrame(results)
print(results_df)

results_df.to_csv("model_evaluation_results.csv", index=False)
