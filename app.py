import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load('employee_income_prediction.joblib')

# 🎉 Title of the app
st.title('💰 **Monthly Income Prediction for Employees** 🚀')

# -------------------------------
# Input Form Section
# -------------------------------
st.subheader('🔍 Please provide the employee details:')

# Input fields based on the dataset columns
gender = st.selectbox('👩‍💼 **Gender**', ['Male', 'Female', 'Other'])
marital_status = st.selectbox('💍 **Marital Status**', ['Single', 'Married', 'Divorced'])
city = st.selectbox('🏙️ **City**', ['Surabaya', 'Jakarta', 'Bandung'])
education_level = st.selectbox('🎓 **Education Level**', ['SMA', 'D3', 'S1', 'S2'])
department = st.selectbox('🏢 **Department**', ['Marketing', 'IT', 'HR', 'Sales', 'Finance'])
income_class = st.selectbox('💸 **Income Class**', ['Low', 'High'])
age = st.number_input('🧑 **Age**', min_value=2, max_value=66, value=35)
years_experience = st.number_input('💼 **Years of Experience**', min_value=0, max_value=24, value=10)
weekly_hours = st.number_input('🕒 **Weekly Hours Worked**', min_value=23, max_value=57, value=40)
bonus_percentage = st.number_input('💵 **Bonus Percentage**', min_value=1, max_value=18, value=10)
performance_score = st.number_input('🏆 **Performance Score**', min_value=44, max_value=107, value=75)
overtime_hours = st.number_input('⏰ **Overtime Hours (Monthly)**', min_value=0, max_value=25, value=10)

# -------------------------------
# Prediction Section
# -------------------------------
if st.button('🔮 **Predict**'):
    # Create a DataFrame with the user input
    input_data = pd.DataFrame({
        'Gender': [gender],
        'Marital Status': [marital_status],
        'City': [city],
        'Department': [department],
        'Income Class': [income_class],
        'Education Level': [education_level],
        'Age': [age],
        'Years Experience': [years_experience],
        'Weekly Hours': [weekly_hours],
        'Bonus Percentage': [bonus_percentage],
        'Performance Score': [performance_score],
        'Overtime Hours': [overtime_hours]
    })

    # -------------------------------
    # Apply the same transformations to the input data
    input_data_transformed = ct.transform(input_data)  # Apply the ColumnTransformer to the input data

    # -------------------------------
    # Make prediction and calculate probability
    pred = model.predict(input_data_transformed)[0]  # Use the transformed data for prediction
    prob = model.predict_proba(input_data_transformed)[0][1]  # Use the transformed data for probability

    # -------------------------------
    # Show results to the user
    st.markdown('### 🏆 **Prediction Results**')

    st.write(f'**💰 Predicted Monthly Income**: {pred} USD')
    st.progress(prob)  # Display the probability as a progress bar
    st.caption(f'💡 **Probability of Income Prediction**: {prob:.2f}')
