import streamlit as st 
import pandas as pd
import db

# Staff 
# 	- Id - unique id  int
# 	- Name -  string
# 	- Contact - int
# 	- Field - string
# 	- time - means entry and exist time normally - time
# 	- status - occupied, free, unavailable - string
# 	- tentative date of availability - date if unavailable.


# - Other hospitals can request staff from other hospitals. 
# - if requested staff is free than it should to assigned task to go to the hospital.
# - our algorithms can suggest alternative staff member that is similar to requested staff member with similar qualification.

# - it will only work if given staff members is free and hospital does not require him/ her in near future.
# - by using past recorded data , we can predict the requirement of hospital as per the time / season.

st.title("STAFF MANAGEMENT")


# data=pd.read_csv("pages\staff_management.csv")
data=pd.read_csv("https://raw.githubusercontent.com/Rjchauhan18/Competition/main/pages/staff_management.csv")
# st.write(data)
selected=st.selectbox("Choose " , data["Hospital name"])

def detail():
        
    fetch_list=db.fetchuing_Staff(selected)
    st.write(len(fetch_list))
    for l in fetch_list:
        st.write("ID : "+l["id"])
        st.write("Name : "+l["name"])
        st.write("Hospital Name : "+l["Hospital_name"])
        st.write("Contact : "+l["Contact"])
        st.write("Field : "+l["Field"])
        st.write("Available : "+l["Availible"])
        st.write("---")
detail()
    # row = data[data["Hospital name"] == selected]

