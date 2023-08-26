import streamlit as st 
import pandas as pd

data=pd.read_csv("pages\staff_management.csv")

st.write(data)
selected=st.selectbox("Choose " , data["Hospital name"])
st.write(selected)