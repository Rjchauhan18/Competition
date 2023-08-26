import streamlit as st
import pandas as pd 


def medicine():
    st.title("MEDICINE STOCK MANAGEMENT ")

    hospitals_data=pd.read_csv("pages\MOCK_DATA.csv")

    selected_hospital = st.selectbox("Available Hospital",hospitals_data["Hospital Name"])
    row = hospitals_data[hospitals_data["Hospital Name"] == selected_hospital]
    col1,col2=st.columns(2)
    col3,col4=st.columns(2)
    with col1:
        st.write("Hospital Name:", row["Hospital Name"])
    with col2:
        st.write("Minimum Stock:", row["Minimum Stock"])

    with col3:
        st.write("Back up:", row["Back up"])

    with col4:
        st.write("Extra:", row["Extra"])
        





      
medicine()