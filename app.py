import streamlit as st
from main import email_list, email, recipe_setup

#######################################################
####### Choose the options for meals this week #######

meal_num = 3
quick_options_only = False

#######################################################
#######################################################

st.title("GoobGrub Weekly Recipes")

if st.button("Generate from All Recipes!"):
    quick_options_only = False
    recipe_setup()
    email(email_list)
    print("Mail has been sent")
    #st.write(email_string)

if st.button("Generate from Quick Recipes!"):
    quick_options_only = True
    recipe_setup()
    email(email_list)
    print("Mail has been sent")