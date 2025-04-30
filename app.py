import streamlit as st
from main import email_list, email, recipe_setup

st.title("GoobGrub Weekly Recipes")

if st.button("Generate Recipes!"):
    recipe_setup()
    email(email_list)
    print("Mail has been sent")
    #st.write(email_string)