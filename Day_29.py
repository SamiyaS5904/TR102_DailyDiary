# STREAMLIT in python 

# https://streamlit.io/     

# for running any program type ----> streamlit run Day_29.py          ( it won't work as direct python program)


import streamlit as st

st.title('BMI CALCULATOR')

col1, col2 = st.columns(2)

with col1:
    name = st.text_input('Enter Your Name')
    height = st.number_input('Enter Your Height (in meters) :')
    height = st.number_input('Enter Your Weight (in kgs) :')

with col2:
    if height > 0 and weight > 0:
        bmi = round(weight/(height**2),2)                      # it rounds of the value till 2 decimal places 
        st.metric(label='BMI', value = bmi)

    
    if bmi<18.5:
        st.warning('')