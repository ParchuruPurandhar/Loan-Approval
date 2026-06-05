import streamlit as st
import pandas as pd
import joblib

# Load model and preprocessor
model = joblib.load("loan_model.pkl")
preprocessor = joblib.load("preprocessor.pkl")

st.title("🏦 Loan Approval Prediction")

age = st.number_input("Age", 18, 80, 30)
income = st.number_input("Income", 0, 1000000, 50000)
credit_score = st.number_input("Credit Score", 300, 900, 700)
loan_amount = st.number_input("Loan Amount", 1000, 1000000, 100000)

if st.button("Predict"):

    data = pd.DataFrame({
        "age":[age],
        "income":[income],
        "savings":[10000],
        "monthly_expenses":[5000],
        "num_dependents":[1],
        "credit_score":[credit_score],
        "loan_amount":[loan_amount],
        "loan_term_months":[36],
        "employment_years":[5],
        "recent_default":[0],
        "has_credit_card":[1],
        "signup_dayofweek":[1],
        "debt_to_income":[0.1],
        "sin_age":[0.5],
        "signup_recency_days":[30],
        "income_per_dependent":[income],
        "home_ownership":["Own"],
        "education":["Bachelors"],
        "marital_status":["Single"],
        "region":["North"]
    })

    transformed = preprocessor.transform(data)

    prediction = model.predict(transformed)[0]

    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")