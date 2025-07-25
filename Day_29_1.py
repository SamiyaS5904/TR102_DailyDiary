## HEALTH CALCULATOR APP

import streamlit as st

st.set_page_config(page_title='Health Calculator')
st.title('All in one Health Calculator')

st.sidebar.header('Enter Your Details')
name = st.sidebar.text_input('Name')
age = st.sidebar.text_input('Age')
gender = st.sidebar.radio('Gender', options=['Male', 'Female'])
height = st.sidebar.number_input('Height (in cm)', min_value=0.0)
weight = st.sidebar.number_input('Weight (in kg)', min_value=0.0)

# Convert height to meters for BMI calculation
height_m = height / 100 if height else 0

bmi_tab, bmr_tab, body_fat_tab, water_intake_tab, ideal_weight_tab = st.tabs(['BMI', 'BMR', 'Body Fat%', 'Water Intake', 'Ideal Weight'])

with bmi_tab:
    st.subheader('Body Mass Index (BMI)')
    if height_m > 0 and weight > 0:
        bmi = round(weight / (height_m ** 2), 2)
        st.metric(label='BMI', value=bmi)

        if bmi < 18.5:
            st.warning(f'Hi {name}, You are Underweight')
        elif 18.5 <= bmi < 24.9:
            st.success(f'Hi {name}, You are Healthy with ideal weight')
        elif 25 <= bmi < 29.9:
            st.error(f'Hi {name}, You are Overweight')
        else:
            st.error(f'Hi {name}, You are Obese')

with bmr_tab:
    st.subheader('Basal Metabolic Rate (BMR)')
    try:
        age = float(age)  # Convert age to float
        base = (10 * weight + 6.25 * height) - (5 * age)
        if gender == 'Male':
            bmr = base + 5
        else:
            bmr = base - 161
        st.success(f'Hi {name}, your body needs at least {round(bmr)} kcal/day to function at rest.')
    except ValueError:
        st.error("Please enter a valid age to calculate BMR.")

with body_fat_tab:
    st.subheader('Body Fat Percentage Calculator')

    neck = st.number_input('Neck (in cm)', min_value=0.0)
    waist = st.number_input('Waist (in cm)', min_value=0.0)

    