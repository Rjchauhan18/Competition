import streamlit as st
import pandas as pd 
import Home 


def medicine():
    st.title("MEDICINE STOCK MANAGEMENT ")

    hospitals_data=pd.read_csv("pages\MOCK_DATA.csv")
    # st.write(hospitals_data)
    # st.write(hospitals_data["Hospital"])
    hospitals_dic=hospitals_data.to_dict()

    # for nm in hospitals_dic:
        # nm_dic={"min":min,"bkup":bkup,"ex":ex}
        # hospital_details["hospital"].update({nm:nm_dic})


        
    # st.write(hospitals_dic)

    selected_hospital = st.selectbox("Available Hospital",hospitals_data["Hospital Name"]) 

    df = hospitals_data[hospitals_data['Hospital Name'].str.contains(selected_hospital)]
    # f= hospitals_data[hospitals_data["Hospital Name"]]==selected_hospital
    st.write(df)

    def Hospital_detail():
        hospital_detail=st.container()
        with hospital_detail:
            st.write(df["Hospital Name"])
    # Hospital_detail() 
      
medicine()