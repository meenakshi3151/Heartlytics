import streamlit as st
import pandas as pd
import pickle
import joblib

model = joblib.load("heart_disease_model.joblib")
pickle.dump(model, open("model_repacked.pkl", "wb"), protocol=4)

FEATURES = [
    'Age', 'Gender', 'Diabetes', 'Health-Insurance', 'Blood-Rel-Stroke',
    'Vigorous-work', 'Annual-Family-Income', 'Uric.Acid', 'Blood-Rel-Diabetes',
    'Glucose', 'Creatinine', 'Total-Cholesterol', 'Glycohemoglobin',
    'Lymphocyte', 'Platelet-count', 'Cholesterol', 'Moderate-work',
    'Red-Cell-Distribution-Width', 'X60-sec-pulse', 'HDL', 'Diastolic',
    'Systolic', 'Monocyte', 'Eosinophils'
]
st.set_page_config(page_title="CardioSense", layout="centered")
st.title("CardioSense")
st.markdown("### Predict Heart Disease Risk based on Health Parameters")
with st.form("heart_disease_form"):
    col1, col2 = st.columns(2)

    with col1:
        Age = st.number_input("Age", min_value=1, max_value=120)
        Gender = st.radio("Gender", ["Male", "Female"])
        Diabetes = st.radio("Diabetes", ["Yes", "No"])
        Health_Insurance = st.radio("Health Insurance", ["Yes", "No"])
        Blood_Rel_Stroke = st.radio("Blood Relative had Stroke?", ["Yes", "No"])
        Vigorous_work = st.radio("Vigorous Work", ["Yes", "No"])
        Moderate_work = st.radio("Moderate Work", ["Yes", "No"])
        Annual_Family_Income = st.number_input("Annual Family Income", min_value=0.0, step=1000.0)
        Uric_Acid = st.number_input("Uric Acid (mg/dL)", min_value=0.0, step=0.1)
        Blood_Rel_Diabetes = st.radio("Blood Relative has Diabetes?", ["Yes", "No"])

    with col2:
        Glucose = st.number_input("Glucose (mg/dL)", min_value=0.0, step=0.1)
        Creatinine = st.number_input("Creatinine (mg/dL)", min_value=0.0, step=0.1)
        Total_Cholesterol = st.number_input("Total Cholesterol (mg/dL)", min_value=0.0, step=1.0)
        Glycohemoglobin = st.number_input("Glycohemoglobin (%)", min_value=0.0, step=0.1)
        Lymphocyte = st.number_input("Lymphocyte Count", min_value=0.0, step=1.0)
        Platelet_count = st.number_input("Platelet Count", min_value=0.0, step=1.0)
        Cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=0.0, step=1.0)
        Red_Cell_Width = st.number_input("Red Cell Distribution Width", min_value=0.0, step=0.1)
        X60_sec_pulse = st.number_input("60-sec Pulse", min_value=0.0, step=1.0)
        HDL = st.number_input("HDL (mg/dL)", min_value=0.0, step=0.1)
        Diastolic = st.number_input("Diastolic BP", min_value=0.0, step=1.0)
        Systolic = st.number_input("Systolic BP", min_value=0.0, step=1.0)
        Monocyte = st.number_input("Monocyte", min_value=0.0, step=0.1)
        Eosinophils = st.number_input("Eosinophils", min_value=0.0, step=0.1)

    submitted = st.form_submit_button("🔍 Predict")

if submitted:
    data = {
        'Age': Age,
        'Gender': 1 if Gender == "Male" else 0,
        'Diabetes': 1 if Diabetes == "Yes" else 0,
        'Health-Insurance': 1 if Health_Insurance == "Yes" else 0,
        'Blood-Rel-Stroke': 1 if Blood_Rel_Stroke == "Yes" else 0,
        'Vigorous-work': 1 if Vigorous_work == "Yes" else 0,
        'Annual-Family-Income': Annual_Family_Income,
        'Uric.Acid': Uric_Acid,
        'Blood-Rel-Diabetes': 1 if Blood_Rel_Diabetes == "Yes" else 0,
        'Glucose': Glucose,
        'Creatinine': Creatinine,
        'Total-Cholesterol': Total_Cholesterol,
        'Glycohemoglobin': Glycohemoglobin,
        'Lymphocyte': Lymphocyte,
        'Platelet-count': Platelet_count,
        'Cholesterol': Cholesterol,
        'Moderate-work': 1 if Moderate_work == "Yes" else 0,
        'Red-Cell-Distribution-Width': Red_Cell_Width,
        'X60-sec-pulse': X60_sec_pulse,
        'HDL': HDL,
        'Diastolic': Diastolic,
        'Systolic': Systolic,
        'Monocyte': Monocyte,
        'Eosinophils': Eosinophils
    }
    input_df = pd.DataFrame([data], columns=FEATURES)
    prediction = model.predict(input_df)[0]
    st.markdown("---")
    if prediction == 1:
        st.error("**Heart Disease Detected!** Please consult a doctor for further evaluation.")
    else:
        st.success("**No Heart Disease Detected.** Keep maintaining a healthy lifestyle!")
