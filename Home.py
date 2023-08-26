import streamlit as st 
import db
import pandas as pd
# import plotly
import plotly.graph_objects as go
import altair as alt

Medicine=300
beds=50

st.set_page_config(page_title="COVIED-19 MANAGEMENT SYSTEM" , page_icon=":bar_chart:", layout="wide")






def app():
    
    if st.sidebar.button('Log Out'):
        st.session_state.loggedIn_user = False
        st.experimental_rerun()
    
    st.title("COVID-19 MANAGEMENT SYSTEM")
    st.write("---")
    data=pd.read_csv("Latest Covid-19 India Status.csv")
    data.rename(columns={"State/UTs": "State"},inplace=True)
    st.table(data)
    
    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter( x=data['State'], y=data['Death Ratio'], name="States"))
        fig.add_trace(go.Scatter(x=data['State'], y=data['Death Ratio'], name="Discharge Ratio"))
        fig.layout.update(
            title_text='Covid-19 State data', xaxis_rangeslider_visible=True)
     
        st.plotly_chart(fig , use_container_width=True)
    plot_raw_data()
    
# app() 





loggedIn_user=None

def signal():
    return loggedIn_user

if 'loggedIn_user' not in st.session_state:
    st.session_state.loggedIn_user=loggedIn_user


def login():
    
        
        Full_name= st.text_input( 'Full_name ')
        email= st.text_input('Email id')
        password= st.text_input('Enter Your Password',type="password")

    
        if st.button('Login'):
            try:
                loggedIn_user=db.fetch_user(Full_name, email,password)
            except:
                pass

            if loggedIn_user == True:
                st.session_state["loggedIn_user"]=loggedIn_user
                st.info("You have successfully logged In")
                # st.stop()
                st.experimental_rerun()
                
            elif loggedIn_user == "Invalid Email ID":
                st.error("Invalid Email ID")
            
            else:
                st.session_state["loggedIn_user"]=loggedIn_user
                
                st.error("Invalid Patient Detail")
                st.warning("Log In failed")
       

if st.session_state.get("loggedIn_user") == True:
    app()

if st.session_state.get("loggedIn_user") == False or st.session_state.get("loggedIn_user") == None:
    st.title("COVID-19 MANAGEMENT SYSTEM")
    
    choice = st.selectbox('Login/SignUp',['Login', 'SignUp'])
    if choice == 'Login':
            login()

    else:
        Full_name= st.text_input('Enter Your Full Name')
        # lt_name= st.text_input('Last Name')
        email= st.text_input('Email ID')
        age= st.text_input('Enter your age')
        phone= st.text_input('Enter Your Phone Number ')
        password= st.text_input('Enter Your Password ', type="password")
        Re_enter= st.text_input('Re-enter your password', type="password")

        if st.button('Create My Account'):
        #   user = auth.create_user( email=email, password=password,uid=username)
            if password==Re_enter:

                created_user=db.create_user(Full_name,email,age,phone,password)
                if created_user == True:
                    st.balloons()

                    st.write('Sucessfully created Account')
                else:
                    st.write(created_user)
                    st.warning('Account creation failed')
            else:
                st.warning("Passowrds Doesn't Match")
                
                
                
        
