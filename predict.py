import pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def load_pickle(x):
    with open(f'saved/{x}.obj', 'rb') as f:
        return pickle.load(f)
    
global variables, scaler, lr, woe_dict

variables = load_pickle('variables')
scaler = load_pickle('scaler')
lr = load_pickle('logistic_model')
woe_dict = variables['WoEDict']

def transform(credit_utility, age, monthly_income, dependents, 
                         debt, open_credit_lines, real_estate, pastdues3059, 
                         pastdues6089, pastdues90):
    
    credit_utility = "Good" if credit_utility <= 0.3 else "Average" if 0.3 < credit_utility <= 0.7 else "Bad"
    age = "Below30" if age <= 30 else "30-40" if 30 < age <= 40 else "40-50" if 40 < age <= 50 else "50-60" if 50 < age <= 60 else "60-00" if 60 < age <= 70 else "Above70"
    monthly_income = "Low-Income" if monthly_income <= 1000 else "Moderate-Income" if 1000 < monthly_income <= 4000 else "Middle-Income" if 4000 < monthly_income <= 7000 else "Upper-Middle-Income" if 7000 < monthly_income <= 10000 else "High-Income" if 10000 < monthly_income <= 15000 else "Rich"
    dependents = "No" if dependents == 0 else "Low" if 0 < dependents <= 2 else "Moderate" if 2 < dependents <= 5 else "High"
    debt = "Low-Debt" if debt <= 0.3 else "Moderate-Debt" if 0.3 < debt <= 1 else "High-Debt"
    open_credit_lines = "Few" if open_credit_lines <= 2 else "Moderate" if 2 < open_credit_lines <= 5 else "Many" if 5 < open_credit_lines <= 10 else "Numerous" if 10 < open_credit_lines <= 15 else "Extensive"
    real_estate = "No-Estate-Loans" if real_estate == 0 else "Low-Estate-Loans" if 0 < real_estate <= 2 else "Moderate-Estate-Loans" if 2 < real_estate <= 4 else "High-Estate-Loans" if 4 < real_estate <= 7 else "Very-High-Estate-Loans"
    pastdues3059 = "No" if pastdues3059 == 0 else "Rare" if 0 < pastdues3059 <= 2 else "Ocassional" if 2 < pastdues3059 <= 5 else "Frequent" if 5 < pastdues3059 <= 10 else "Very-Frequent"
    pastdues6089 = "No" if pastdues6089 == 0 else "Rare" if 0 < pastdues6089 <= 2 else "Ocassional" if 2 < pastdues6089 <= 5 else "Frequent"
    pastdues90 = "No" if pastdues90 == 0 else "Rare" if 0 < pastdues90 <= 2 else "Ocassional" if 2 < pastdues90 <= 5 else "Frequent" if 5 < pastdues90 <= 10 else "Very-Frequent"

    credit_utility = woe_dict['CreditUtility'].get(credit_utility)
    age = woe_dict['Age'].get(age)
    monthly_income = woe_dict['Monthly-Income'].get(monthly_income)
    dependents = woe_dict['Dependents'].get(dependents)
    debt = woe_dict['Debt'].get(debt)
    open_credit_lines = woe_dict['OpenCreditLines'].get(open_credit_lines)
    real_estate = woe_dict['RealEstateLoans'].get(real_estate)
    pastdues3059 = woe_dict['30-59DaysLatePayment'].get(pastdues3059)
    pastdues6089 = woe_dict['60-89DaysLatePayment'].get(pastdues6089)
    pastdues90 = woe_dict['90DaysLatePayment'].get(pastdues90)

    input = np.array([credit_utility, age, pastdues3059, debt, monthly_income, open_credit_lines, pastdues90, real_estate, pastdues6089, dependents])
    input = scaler.transform(input.reshape(1, -1))

    return input

def predict_credit_default(array):
    predict = lr.predict(array)
    return "Loan Not Approved" if predict==1 else "Loan Approved"

if __name__=="__main__":
    input_array = transform(0.2, 34, 5000, 2, 0.4, 3, 1, 0, 0, 0)
    result = predict_credit_default(input_array)
    print(result)
