# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:53:57 2023

@author: User
"""

# Imports
import streamlit as st
import joblib
import os
from pathlib import Path



def main():
    
    html_temp = """
    <div style = "background-color:lightblue; padding:16px">
    <h2 style = "color: black; text-align: center;"> Health Insurace Cost Prediction using ML
    
    </h2>
    
    </div>
    
    """
    
    st.markdown(html_temp, unsafe_allow_html = True)
    
    # model = joblib.load("C:/Users/User/.spyder-py3/model_joblib_gr")
    
    pkl_pathl = Path(__file__).parents[1] /'model_joblib_gr'
    model = joblib.load('model_joblib_gr')
    
    # Input ranges match the training data (insurance.csv): age 18-64, BMI 15.96-53.13, 0-5 children
    p1 = st.slider('Enter your age', 18, 64)
    
    s1 = st.selectbox('Sex', ('Male', 'Female'))
    
    if s1 == 'Male':
        p2 = 1
    else:
        p2 = 0
        
    p3 = st.number_input('Enter your BMI value', min_value = 15.96, max_value = 53.13, value = 30.4)
        
    p4 = st.slider('Enter Number of Children', 0,5)
    
    s2 = st.selectbox('Smoker', ('Yes', 'No'))
    
    if s2 == 'Yes':
        p5 = 1
    else:
        p5 = 0
        
    s3 = st.selectbox('Select Region', ('southwest', 'southeast', 'northwest', 'northeast'))
    
    # Same encoding as training: southwest 1, southeast 2, northwest 3, northeast 4
    if s3 == 'southwest':
        p6 = 1
    elif s3 == 'southeast':
        p6 = 2
    elif s3 == 'northwest':
        p6 = 3
    else:
        p6 = 4
        
    if st.button('Predict'):
        pred = model.predict([[p1,p2,p3,p4,p5,p6]])
        st.balloons()
        st.success('Your Insurance cost is {}'.format(round(pred[0], 2)))
    
    
if __name__ == '__main__':
    main()

