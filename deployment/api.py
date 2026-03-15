from fastapi import FastAPI
import pickle
import numpy as np

# Create API
app = FastAPI()

# Load trained model
with open("churn_model.pkl", "rb") as file:
    model = pickle.load(file)


# Home route
@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API"}


# Prediction route
@app.post("/predict")
def predict(contract: int, paperless: int, payment: int):
    try:
        data = np.array([[contract, paperless, payment, 0, 0, 0, 0, 0, 0]])
        prediction = model.predict(data)

        if prediction[0] == 1:
            return {"prediction": "Customer will churn"}
        else:
            return {"prediction": "Customer will stay"}

    except Exception as e:
        return {"error": str(e)}
