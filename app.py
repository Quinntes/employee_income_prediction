import streamlit as st
import joblib
import pandas as pd

# Muat model dan preprocessing pipeline
model = joblib.load('employee_income_prediction.joblib')
ct = joblib.load('preprocessing_pipeline.joblib')

# 🎉 Title of the app
st.title('💰 **Monthly Income Prediction for Employees** 🚀')

# -------------------------------
# Input Form Section
# -------------------------------
st.subheader('🔍 Please provide the employee details:')

# Input fields
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
# Prepare the input data
# -------------------------------
input_data = pd.DataFrame({
    'gender': [gender],
    'marital_status': [marital_status],
    'city': [city],
    'department': [department],
    'income_class': [income_class],
    'education_level': [education_level],
    'age': [age],
    'years_experience': [years_experience],
    'weekly_hours': [weekly_hours],
    'bonus_percentage': [bonus_percentage],
    'performance_score': [performance_score],
    'overtime_hours': [overtime_hours]
})

# -------------------------------
# Apply preprocessing to the input data
# -------------------------------
input_transformed = ct.transform(input_data)

# -------------------------------
# Make prediction
# -------------------------------
if st.button('🔮 **Predict**'):
    # Prediksi pendapatan bulanan (model regresi)
    pred = model.predict(input_transformed)[0]

    # Format prediksi dengan hanya dua angka di belakang koma
    pred_formatted = f"{pred:,.2f}"  # Format angka dengan dua angka di belakang koma dan koma sebagai pemisah ribuan

    # Ganti titik dengan koma untuk format desimal Indonesia
    pred_formatted = pred_formatted.replace(',', ' ').replace('.', ',')

    # -------------------------------
    # Show results to the user
    # -------------------------------
    st.markdown('### 🏆 **Prediction Results**')
    st.write(f'**💰 Predicted Monthly Income**: {pred_formatted} IDR')

    # Rentang pendapatan untuk progress bar
    min_income = 878  # 878 USD
    max_income = 148880  # 148 ribu USD

    # Perhitungan progress, pastikan berada di dalam rentang [0, 1]
    progress_value = (pred - min_income) / (max_income - min_income)

    # Batasi nilai progress dalam rentang [0, 1]
    progress_value = max(0, min(1, progress_value))

    # Menampilkan progress bar berdasarkan nilai yang sudah dibatasi
    st.progress(progress_value)  # Rentang berdasarkan min dan max
