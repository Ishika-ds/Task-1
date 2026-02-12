#  House Price Prediction using Machine Learning

##  Project Overview

This project builds and compares multiple Machine Learning models to predict house prices based on property features such as:

- Area  
- Bedrooms  
- Bathrooms  
- Age  
- Location  
- Property Type  

The objective is to analyze model performance and determine the best regression model for accurate price prediction.

---

## 🛠️ Technologies Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-learn  

---

##  Project Structure

-house_prices.csv
-9th_task.py
-model_evaluation_report.md
-predictions_vs_actual.png


---

##  Implementation Workflow

1. Data Loading and Exploration  
2. Data Preprocessing  
   - Handling missing values  
   - Encoding categorical variables  
3. Train-Test Split (80% Training, 20% Testing)  
4. Model Training:
   - Linear Regression  
   - Decision Tree Regressor  
   - Random Forest Regressor  
5. Model Evaluation using:
   - Mean Absolute Error (MAE)  
   - Mean Squared Error (MSE)  
   - R² Score  
6. Feature Importance Analysis  
7. Visualization of Predictions vs Actual Prices  

---

##  Model Performance

| Model | MAE | MSE | R² Score |
|-------|------|-------------|-----------|
| Linear Regression | 2,188,736 | 8.45e12 | 0.9406 |
| Decision Tree | 2,280,000 | 9.16e12 | 0.9356 |
| Random Forest | **1,493,949** | **4.12e12** | **0.9711** |

---

##  Best Model

**Random Forest Regressor**

- Lowest MAE and MSE  
- Highest R² score (97.11%)  
- Provides meaningful feature importance  

---

##  Feature Importance (Random Forest)

1. Area – Most influential feature  
2. Location (Rural, Suburb)  
3. Bedrooms  
4. Age  
5. Bathrooms  
6. Property Type  

---

##  Visualization

The project includes a scatter plot comparing actual vs predicted house prices to visually evaluate model accuracy.

---

##  How to Run

1. Install dependencies:
pip install pandas numpy matplotlib scikit-learn


2. Run the script:
python 9th_task.py


---

## 📌 Conclusion

- Random Forest performed best among all models.
- Area and Location are dominant factors influencing house price.
- Ensemble models provide better generalization compared to single regression models.
- The project demonstrates a complete machine learning workflow from preprocessing to evaluation.

---




















