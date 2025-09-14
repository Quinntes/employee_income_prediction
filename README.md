# Employee Monthly Income Prediction

This project focuses on predicting **employee monthly income** based on various factors such as department, city, education level, years of experience, and more. The model was built using various regression techniques, with a focus on optimizing employee compensation packages and understanding key factors that influence salary structures.

---

## Table of Contents

1. [Business Problem](#business-problem)
2. [Objectives](#objectives)
3. [Data Overview](#data-overview)
4. [Data Preprocessing](#data-preprocessing)
5. [Modeling](#modeling)
6. [Evaluation Metrics](#evaluation-metrics)
7. [Feature Importance](#feature-importance)
8. [Conclusion and Recommendations](#conclusion-and-recommendations)
9. [Model Deployment](#model-deployment)
10. [Usage](#usage)

---

## Business Problem

Organizations need to optimize compensation packages for their employees, ensuring fair and competitive pay. The goal is to predict employee **monthly income** based on a variety of factors like **education level**, **years of experience**, **performance score**, and **department**. This allows companies to make informed, data-driven decisions regarding compensation, salary equity, and financial planning.

By using regression models, we can analyze the relationship between employee characteristics (independent variables) and their monthly income (dependent variable), helping HR departments develop fair pay structures and identify pay gaps.

---

## Objectives

* **Salary Prediction**: Predict the monthly income of employees based on features like experience, education, and department.
* **Identify Pay Gaps**: Uncover disparities in salaries among employees with similar profiles, promoting fair pay.
* **Effective Budgeting**: Enable more accurate forecasting of salary expenses for better financial planning.
* **Data-Driven HR Decisions**: Provide HR with actionable insights into the factors influencing compensation.

---

## Data Overview

The dataset used contains various employee attributes such as:

* **employee\_id**: Unique identifier for each employee
* **age**: Age of the employee
* **gender**: Gender of the employee
* **marital\_status**: Marital status
* **city**: City where the employee works
* **education\_level**: Education level of the employee
* **years\_experience**: Work experience in years
* **weekly\_hours**: Weekly working hours
* **department**: Department in which the employee works
* **bonus\_percentage**: Annual bonus percentage
* **performance\_score**: Performance score of the employee
* **overtime\_hours**: Monthly overtime hours worked
* **monthly\_income**: Target variable (monthly income)

---

## Data Preprocessing

* **Missing Data Handling**: Used `SimpleImputer` to handle missing values in both categorical and numerical features.
* **Feature Engineering**: Converted categorical features into numerical values using **One-Hot Encoding** and **Ordinal Encoding** for ordinal variables like `education_level`.
* **Outlier Detection**: Applied the **Z-score** method to detect and remove outliers in numerical features.
* **Scaling**: Scaled numerical features using **RobustScaler** to ensure robustness against outliers.
* **Data Splitting**: Split the data into **training** and **test** sets using an **80-20 split** for model validation.

---

## Modeling

### Models Used:

* **Linear Models**: Ridge, Lasso, ElasticNet, Linear Regression
* **Robust Models**: Huber Regressor, RANSAC
* **Ensemble Models**: Random Forest, Gradient Boosting, XGBoost, LightGBM, CatBoost
* **Non-Linear Models**: Decision Tree, K-Nearest Neighbors, Support Vector Regressor (SVR)

The models were evaluated using cross-validation and were tested against a variety of performance metrics to determine the best predictor for **monthly income**.

### Hyperparameter Tuning:

The best model, **Huber Regressor**, was tuned using **RandomizedSearchCV** to find the optimal combination of hyperparameters, improving the model's accuracy further.

---

## Evaluation Metrics

The following metrics were used to evaluate model performance:

* **Root Mean Squared Error (RMSE)**: Measures the average squared difference between predicted and actual values.
* **Mean Absolute Error (MAE)**: Represents the average absolute errors.
* **Mean Absolute Percentage Error (MAPE)**: Indicates the average percentage error in predictions.
* **R-squared (R²)**: The proportion of variance in the target variable explained by the model.
* **Maximum Error**: Measures the worst-case error in predictions.

---

## Feature Importance

The **Huber Regressor** model was used to determine the importance of each feature based on its coefficient magnitude. The top 5 most important features were:

1. **department\_IT**
2. **city\_Surabaya**
3. **department\_Marketing**
4. **marital\_status\_Single**
5. **bonus\_percentage**

These insights can help businesses prioritize the most influential factors when adjusting salary structures or setting pay scales.

---

## Conclusion and Recommendations

### Conclusion:

* **Huber Regressor** proved to be the best model for predicting employee salaries, outperforming others like **CatBoost** in terms of RMSE, MAE, and MAPE.
* The key features influencing employee income are **department** and **city**, while factors like **marital status** and **bonus percentage** have minimal impact.
* **Log Transformation** of the target variable did not significantly improve performance, confirming that the **Huber Regressor (standard version)** remains the preferred model.

### Recommendations:

* Use **Huber Regressor** to predict monthly income and optimize employee compensation strategies.
* Focus on addressing pay disparities between employees, especially those in different departments or cities.
* HR can use the model to predict future salary expenses, enabling more accurate financial planning.
* Leverage the model’s insights to implement fair and competitive pay structures that promote employee satisfaction and retention.

---

## Model Deployment

The final trained model and preprocessing pipeline are saved using **Joblib** for easy deployment in production environments.

* **Model**: Huber Regressor (best model after hyperparameter tuning)
* **Preprocessing Pipeline**: Includes imputation, scaling, and encoding transformations

Both the model and pipeline are available for loading and making predictions in future applications.

---

## Usage

To use the trained model for new predictions, follow these steps:

1. Load the saved model and preprocessing pipeline using **Joblib**.
2. Preprocess new data using the same pipeline (feature scaling, encoding, etc.).
3. Pass the preprocessed data into the model for salary prediction.

### Example:

```python
import joblib
import pandas as pd

# Load the model and preprocessing pipeline
model = joblib.load('employee_income_prediction.joblib')
preprocessor = joblib.load('preprocessing_pipeline.joblib')

# Example new employee data
new_data = pd.DataFrame([
    {'gender': 'Male', 'marital_status': 'Single', 'city': 'Bangalore', 'education_level': 'Bachelors', 'department': 'IT', 'income_class': 'High', 'age': 28, 'years_experience': 3, 'weekly_hours': 40, 'bonus_percentage': 10, 'performance_score': 4.5, 'overtime_hours': 5}
])

# Preprocess the data
processed_data = preprocessor.transform(new_data)

# Make prediction
predicted_income = model.predict(processed_data)
print(f"Predicted Monthly Income: {predicted_income[0]}")
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Quinntes/employee_income_prediction/blob/main/LICENSE) file for more information.