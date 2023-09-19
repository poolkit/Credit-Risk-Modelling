import streamlit as st
from predict import transform, predict_credit_default

st.set_page_config(
    page_title="Credit Default Prediction POC",
    page_icon=":money_with_wings:"
)

st.markdown(
    """
    <style>
    body {
        background-image: url('https://blogs.ibo.org/files/2016/08/parachute-introvertoptimized.jpg');
        background-size: cover;
    }
    .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
    .btn {
        display: block;
        margin-top: 20px;
        background-color: #0072B5;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .btn:hover {
        background-color: #005685;
    }
    .approved {
        color: green;
    }
    .not-approved {
        color: red;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("Credit Default Prediction")

col1, col2 = st.columns(2)
credit_utility = col1.number_input('Credit Utility')
age = col2.number_input("Age", step=1)
monthly_income = col1.number_input("Monthly Income", step=100)
dependents = col2.number_input("Dependents", step=1)
debt = col1.number_input("Debt Ratio")
open_credit_lines = col2.number_input("Open Credit Lines", step=1)
real_estate = col1.number_input("Real Estate Loans", step=1)
pastdues3059 = col2.number_input("30-59DaysLatePayment", step=1)
pastdues6089 = col1.number_input("60-89DaysLatePayment", step=1)
pastdues90 = col2.number_input("90DaysLatePayment", step=1)

inputs = [credit_utility, age, monthly_income, dependents, 
                         debt, open_credit_lines, real_estate, pastdues3059, 
                         pastdues6089, pastdues90]

if st.button("Predict"):
    input_array = transform(credit_utility, age, monthly_income, dependents, 
                         debt, open_credit_lines, real_estate, pastdues3059, 
                         pastdues6089, pastdues90)
    prediction = predict_credit_default(input_array)

    if all(x == 0 for x in inputs):
        st.warning("Please fill the form.")
    elif age<18:
        st.warning("Age can not be less than 18.")
    else:
        if prediction == "Loan Approved":
            st.success("Loan Approved")
        elif prediction == "Loan Not Approved":
            st.error("Loan Not Approved")
    
    # st.success(f"Credit Default Prediction: {result}")






