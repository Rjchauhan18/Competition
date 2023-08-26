import streamlit as st 
import pandas as pd


st.title("STAFF MANAGEMENT")


data=pd.read_csv("pages\staff_management.csv")
# data=pd.read_csv("https://raw.githubusercontent.com/Rjchauhan18/Competition/main/pages/staff_management.csv")
st.write(data)
selected=st.selectbox("Choose " , data["Hospital name"])

st.write(selected)