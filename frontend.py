import streamlit as st
import requests
api_url="http://127.0.0.1:8000/predict"
st.title("Insurance Premium Category Predictor")
st.markdown("Enter the below details")
age=st.number_input("Age",min_value=1,max_value=120,value=20)
weight=st.number_input("weight(kg)",min_value=1.0,value=65.0)
height=st.number_input("height (m)" ,min_value=0.5,max_value=2.5,value=1.7)
income_lpa=st.number_input("Annual_income(LPA)",min_value=1.0,value=2.4)
smoker=st.selectbox(" Are you a smoker?",options=[True,False])
city=st.text_input("City",value="Delhi")
occupation=st.selectbox("Occupation",options=['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'])

if st.button("Predict Premium Category"):
    input_data={
        "age":age,
        "weight":weight,
        "height":height,
        "income_lpa":income_lpa,
        "smoker":smoker,
        "city":city,
        "occupation":occupation

    }
    try:
        response=requests.post(api_url,json=input_data)
        if response.status_code==200:
            result=response.json()
            st.success(f"Predicted Insurance Premium Category: **{result['predicted_category']}**")
        else:
            st.error(f"Api Error:{response.status_code}-{response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to fast api server")


