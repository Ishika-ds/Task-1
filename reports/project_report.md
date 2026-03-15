# Customer Churn Prediction Project Report

## Introduction
Customer churn is a major challenge for companies, especially in telecom and subscription-based services. Predicting churn helps businesses identify customers who are likely to leave and take preventive actions to retain them. This project develops a machine learning model to predict customer churn based on customer behavior and service-related features.

## Objective
The objective of this project is to build an end-to-end machine learning system that can predict whether a customer is likely to churn. The system includes data preprocessing, model training, evaluation, and deployment using an API.

## Dataset
The dataset used for this project contains customer information such as contract type, billing preferences, payment method, and other service-related attributes. These features are used to train a machine learning model that predicts whether a customer will churn.

## Methodology
The following steps were followed in this project:

1. **Data Loading** – Importing the dataset for analysis.
2. **Exploratory Data Analysis (EDA)** – Understanding the dataset and identifying patterns.
3. **Data Preprocessing** – Cleaning the data, handling missing values, and encoding categorical variables.
4. **Train-Test Split** – Dividing the dataset into training and testing sets.
5. **Model Training** – Training a machine learning model to learn patterns from the data.
6. **Model Evaluation** – Evaluating model performance using accuracy and other metrics.
7. **Model Saving** – Saving the trained model as a `.pkl` file.
8. **API Deployment** – Deploying the model using FastAPI for real-time predictions.

## Model Used
A Random Forest Classifier was used to train the churn prediction model. Random Forest works by combining multiple decision trees to improve prediction accuracy and reduce overfitting.

## Deployment
The trained model was deployed using FastAPI. The API allows users to send customer feature values and receive predictions about whether the customer will churn. The API can be accessed using a local server and tested through Swagger UI.

## Results
The trained model achieved high prediction accuracy and can effectively classify customers into churn or non-churn categories based on their features.

## Conclusion
This project demonstrates the complete lifecycle of a machine learning application, from data analysis and model training to deployment. Such systems can help companies proactively identify customers at risk of leaving and take steps to improve customer retention.

## Future Improvements
- Improve feature engineering
- Train additional machine learning models for comparison
- Deploy the system on a cloud platform
- Develop a user interface for easier interaction with the model
