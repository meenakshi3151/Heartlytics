import streamlit as st
import pandas as pd
import joblib

model = joblib.load("xgbm_model_with_tuned_params.pkl")

FEATURES = [
    'Age', 'Systolic', 'Pulse Pressure', 'Lymphocyte',
    'Platelet-count', 'Cholesterol', 'Creatinine', 'Glucose', 
    'Glycohemoglobin'
]

st.set_page_config(page_title="Heartlytics", layout="centered")
st.title("Heartlytics")
st.markdown("### Predict Heart Disease Risk based on Key Health Indicators")

with st.form("heart_disease_form"):
    col1, col2 = st.columns(2)

    with col1:
        Age = st.number_input("Age", min_value=1, max_value=120)
        Systolic = st.number_input("Systolic BP", min_value=50, max_value=250)
        Diastolic = st.number_input("Diastolic BP", min_value=30, max_value=150)
        Lymphocyte = st.number_input("Lymphocyte Count", min_value=0)
        Platelet_count = st.number_input("Platelet Count", min_value=0)

    with col2:
        Cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=0.0, step=1.0)
        Creatinine = st.number_input("Creatinine (mg/dL)", min_value=0.0, step=0.01)
        Glucose = st.number_input("Glucose (mg/dL)", min_value=0.0, step=0.1)
        Glycohemoglobin = st.number_input("Glycohemoglobin (%)", min_value=0.0, step=0.1)

    submitted = st.form_submit_button("Predict")

if submitted:
    
    Pulse_Pressure = Systolic - Diastolic  

    data = {
        'Age': Age,
        'Systolic': Systolic,
        'Pulse Pressure': Pulse_Pressure,
        'Lymphocyte': Lymphocyte,
        'Platelet-count': Platelet_count,
        'Cholesterol': Cholesterol,
        'Creatinine': Creatinine,
        'Glucose': Glucose,
        'Glycohemoglobin': Glycohemoglobin
    }

    input_df = pd.DataFrame([data], columns=FEATURES)
    prediction = model.predict(input_df)[0]

    st.markdown("---")

    if prediction == 1:
        st.error("**Heart Disease Detected!** Please consult a cardiologist for further evaluation.")
    else:
        st.success("**No Heart Disease Detected.** Keep maintaining a healthy lifestyle!")
