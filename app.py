import streamlit as st
from main import email_list, yield_string, email, recipe_setup

global quick_options_only
global meal_num
global recipe_string

st.title("GoobGrub")

# Let the user choose how many meals to generate (between 1 and 7)
meal_num = st.number_input("How many meals do you want?", min_value=1, max_value=7, value=3)

if st.button("Generate from All Recipes!"):
    quick_options_only = False
    recipe_setup(quick_options_only, meal_num)
    recipe_string = yield_string()
    #email(email_list)
    #print("Mail has been sent")
    st.text(recipe_string)

if st.button("Generate from Quick Recipes!"):
    quick_options_only = True
    recipe_setup(quick_options_only, meal_num)
    recipe_string = yield_string()
    #email(email_list)
    #print("Mail has been sent")
    st.text(recipe_string)