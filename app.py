import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('model.pkl')

st.set_page_config(page_title="Medical Insurance Predictor", layout="centered")
st.title("💰 Medical Insurance Cost Predictor")
st.markdown("Enter your personal and lifestyle details to estimate your medical insurance charges.")

# User Inputs
age = st.slider("Age", 18, 100, 30)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
children = st.slider("Number of Children", 0, 5, 1)
smoker = st.selectbox("Do you smoke?", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Prepare input data
if st.button("Predict Insurance Cost"):
    input_data = {
    'age': age,
    'sex': 0 if sex == 'male' else 1,
    'bmi': bmi,
    'children': children,
    'smoker': 0 if smoker == 'yes' else 1,
    'region': {
        'southeast': 0,
        'southwest': 1,
        'northeast': 2,
        'northwest': 3
    }[region]
}



    input_df = pd.DataFrame([input_data])

    # Make prediction
    prediction = model.predict(input_df)[0]

    # Show result
    st.success(f"Estimated Medical Insurance Cost: 💲{prediction:,.2f}")
