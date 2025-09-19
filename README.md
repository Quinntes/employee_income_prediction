Berikut revisi README yang lebih konsisten, ringkas, dan selaras dengan seluruh analisis yang telah kamu lakukan:

---

# Employee Monthly Income Prediction

This project aims to predict **employee monthly income** using regression models based on various features such as department, city, education level, experience, and performance. The goal is to support **data-driven compensation planning**, uncover **pay disparities**, and guide **HR and finance decisions** with interpretable insights.

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

Companies need to ensure fair, competitive, and scalable compensation structures. Predicting **monthly income** based on employee attributes enables HR teams to:

- Identify salary inconsistencies  
- Forecast compensation budgets  
- Align pay with performance and role  
- Promote fairness and retention

---

## Objectives

- **Predict Monthly Income** using employee features  
- **Detect Pay Gaps** among similar profiles  
- **Support Budgeting** with accurate salary forecasts  
- **Enable Data-Driven HR Decisions** on promotions, raises, and bonuses  

---

## Data Overview

The dataset includes:

- Demographics: `age`, `gender`, `marital_status`, `city`  
- Qualifications: `education_level`, `years_experience`  
- Workload: `weekly_hours`, `overtime_hours`  
- Performance: `performance_score`, `bonus_percentage`, `income_class`  
- Organizational: `department`  
- Target: `monthly_income`  

---

## Data Preprocessing

- **Missing Values**: Handled using `SimpleImputer`  
- **Encoding**: One-Hot for nominal, Ordinal for ordered features  
- **Outlier Removal**: Z-score method  
- **Scaling**: `RobustScaler` for numerical features  
- **Splitting**: 80/20 train-test split  

---

## Modeling

### Models Evaluated

- **Linear**: Ridge, Lasso, ElasticNet, Linear Regression  
- **Robust**: Huber Regressor, RANSAC  
- **Ensemble**: Random Forest, Gradient Boosting, XGBoost, LightGBM, CatBoost  
- **Non-Linear**: SVR, Decision Tree, KNN  

### Final Model Selection

- **Huber Regressor (Standard)** was selected for its balance of robustness and interpretability.  
- **Hyperparameter Tuning** via `RandomizedSearchCV` yielded minimal gains, confirming the default configuration as optimal.

---

## Evaluation Metrics

- **MedAE**: Median Absolute Error (primary metric)  
- **MAE**: Mean Absolute Error  
- **MAPE**: Mean Absolute Percentage Error  
- **R²**: Explained variance  
- **MaxError**: Worst-case deviation  

---

## Feature Importance

Using Huber Regressor coefficients, the top 5 influential features are:

1. **department_IT**  
2. **city_Surabaya**  
3. **department_Marketing**  
4. **marital_status_Single**  
5. **marital_status_Married**

These insights highlight the impact of organizational and geographic factors on salary, while personal demographics like marital status have minimal influence.

---

## Conclusion and Recommendations

### Conclusion

- **Huber Regressor (Standard)** is the most consistent and accurate model across all prioritized metrics.  
- **Log Transformation** offered minor improvements but did not outperform the standard version.  
- **Key Drivers** of income include department and city, while marital status and bonus percentage are less impactful.

### Recommendations

- Use the model to **optimize compensation** based on role, location, and performance.  
- Identify and address **pay disparities** across departments and cities.  
- Support **budgeting and forecasting** with reliable salary predictions.  
- Design **retention strategies** informed by compensation fairness.  
- Empower HR with **data-driven decisions** on raises, promotions, and bonuses.

---

## Model Deployment

Saved using `Joblib`:

- **Model**: Huber Regressor (final tuned version)  
- **Pipeline**: Includes imputation, scaling, and encoding  

Strealit:
See in the [streamlit] folder.

Tableau:
See the [TABLEAU Dashboard](https://public.tableau.com/views/employee_income_prediction/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link) for details.

Ready for integration into production systems for real-time predictions.

---

## Usage

```python
import joblib
import pandas as pd

# Load model and pipeline
model = joblib.load('employee_income_prediction.joblib')
preprocessor = joblib.load('preprocessing_pipeline.joblib')

# New employee data
new_data = pd.DataFrame([{
    'gender': 'Male',
    'marital_status': 'Single',
    'city': 'Bangalore',
    'education_level': 'Bachelors',
    'department': 'IT',
    'income_class': 'High',
    'age': 28,
    'years_experience': 3,
    'weekly_hours': 40,
    'bonus_percentage': 10,
    'performance_score': 4.5,
    'overtime_hours': 5
}])

# Preprocess and predict
processed = preprocessor.transform(new_data)
predicted_income = model.predict(processed)
print(f"Predicted Monthly Income: {predicted_income[0]}")
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Quinntes/employee_income_prediction/blob/main/LICENSE) for details.