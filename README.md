# Customer Churn Prediction System

## Project Overview
This project builds an end-to-end Machine Learning system to predict whether a telecom customer is likely to churn. Customer churn refers to customers leaving a service provider. By analyzing customer attributes such as contract type, billing method, and payment method, the system predicts the probability of churn.

The trained model is deployed using an API so predictions can be accessed through HTTP requests.

---

## Objectives
- Analyze telecom customer data
- Perform data preprocessing
- Train and evaluate machine learning models
- Save the trained model
- Deploy the model using an API for real-time predictions

---

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Uvicorn

---


## Machine Learning Workflow
1. Data Loading  
2. Exploratory Data Analysis (EDA)  
3. Data Preprocessing  
4. Feature Selection  
5. Model Training  
6. Model Evaluation  
7. Model Saving  
8. API Deployment  

---

## Model Used
Random Forest Classifier

The trained model is saved as:

churn_model.pkl

---

## API Deployment

Install dependencies:

pip install fastapi uvicorn scikit-learn pandas numpy

Run the API:

python -m uvicorn api:app --reload

Open the API documentation in your browser:

http://127.0.0.1:8000/docs

---

## Example Prediction Request

POST request to:

/predict

Example parameters:

contract = 1  
paperless = 1  
payment = 2  

The API returns the predicted churn result.

---

## Future Improvements
- Improve feature engineering
- Try additional machine learning models
- Deploy the API on cloud platforms
- Build a simple web interface for predictions

---

## Conclusion
This project demonstrates the complete lifecycle of a machine learning application, from data analysis and model training to deployment using an API.
