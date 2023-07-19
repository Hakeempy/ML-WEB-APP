# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:53:57 2023

@author: User
"""

# Imports
import streamlit as st
import joblib

def main():
    
    html_temp = """
    <div style = "background-color:lightblue; padding:16px">
    <h2 style = "color: black; text-align: center;"> Health Insurace Cost Prediction using ML
    
    </h2>
    
    </div>
    
    """
    
    st.markdown(html_temp, unsafe_allow_html = True)
    
    model = joblib.load('C:/Users/User/Desktop/Dataset Trials/ML/model_joblib_gr')
    
    p1 = st.slider('Enter your age', 18, 100)
    
    s1 = st.selectbox('Sex', ('Male', 'Female'))
    
    if s1 == 'Male':
        p2 = 1
    else:
        p2 = 0
        
    p3 = st.number_input('Enter your BMI value')
        
    p4 = st.slider('Enter Number of Children', 0,4)
    
    s2 = st.selectbox('Smoker', ('Yes', 'No'))
    
    if s2 == 'Yes':
        p5 = 1
    else:
        p5 = 0
        
    s3 = st.selectbox('Select Region', ('southwest', 'southeast', 'northwest', 'northeast'))
    
    if s3 == 'southwest':
        p6 = 1
    elif s3 == 'southeast':
        p6 = 2
    elif s3 == 'southwest':
        p6 = 3
    else:
        p6 = 4
        
    if st.button('Predict'):
        pred = model.predict([[p1,p2,p3,p4,p5,p6]])
        st.balloons()
        st.success('Your Insurance cost is {}'.format(round(pred[0], 2)))
    
    
if __name__ == '__main__':
    main()

