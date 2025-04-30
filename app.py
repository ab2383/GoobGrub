import streamlit as st
from main import email_list, email, recipe_setup

global quick_options_only
global meal_num
meal_num = 3

st.title("GoobGrub Weekly Recipes")

# Let the user choose how many meals to generate (between 1 and 4)
meal_num = st.number_input("How many meals do you want?", min_value=1, max_value=4, value=3)

if st.button("Generate from All Recipes!"):
    quick_options_only = False
    recipe_setup(quick_options_only, meal_num)
    email(email_list)
    print("Mail has been sent")
    #st.write(email_string)

if st.button("Generate from Quick Recipes!"):
    quick_options_only = True
    recipe_setup(quick_options_only, meal_num)
    email(email_list)
    print("Mail has been sent")