import streamlit as st
import requests
import json

st.header("DEEP DTA")
form = st.form("prediction_form")
drug = form.text_input("Enter drug")
target = form.text_input("Enter target")
submit_button = form.form_submit_button("Predict")

if submit_button == True:
    response = requests.get(f"https://deepdta.onrender.com/prediction?drug={drug}&target={target}")
    result = json.loads(response.text)
    st.write("Binding Affinity",result["Predicted affinity"])
