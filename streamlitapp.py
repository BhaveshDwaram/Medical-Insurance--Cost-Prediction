import numpy as np
import pickle
import pandas as pd
import streamlit as st 


pickle_in = open("linear_regression.pkl","rb")
linear_regression=pickle.load(pickle_in)

def welcome():
    return "Welcome All"


def predict_medical_insurance_cost(age,sex,bmi,children,smoker,region):
    
    prediction=linear_regression.predict([[age,sex,bmi,children,smoker,region]])
    print(prediction)
    return prediction



def main():
    st.title("Medical Insurance Cost Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Medical Insurance Cost Prediction </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("age","")
    sex = st.text_input("sex","")
    bmi = st.text_input("bmi","")
    children = st.text_input("children","")
    smoker = st.text_input("smoker","")
    region = st.text_input("region","")
    result=""
    if st.button("Predict"):
        result=predict_medical_insurance_cost(int(age),int(sex),float(bmi),int(children),int(smoker),int(region))
    st.success('The approximate medical insurance cost  is {} rupess only'.format(int(result)))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    

    