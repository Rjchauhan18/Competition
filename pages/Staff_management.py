import streamlit as st 
import pandas as pd

data=pd.read_csv("pages\staff_management.csv")

st.write(data)