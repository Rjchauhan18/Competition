import streamlit as st 
import db


import pandas as pd
import plotly.graph_objects as go
import altair as alt
import plotly.express as px
from streamlit_lottie import st_lottie
import requests

Medicine=300
beds=50

st.set_page_config(page_title="COVIED-19 MANAGEMENT SYSTEM" , page_icon=":bar_chart:", layout="wide")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



def app(username):
    
    st.sidebar.title(f"Welcome, {username}")
    if st.sidebar.button('Log Out'):
        st.session_state.loggedIn_user = False
        st.experimental_rerun()
    
    st.title("COVID-19 MANAGEMENT SYSTEM")
    st.write("---")
    data=pd.read_csv("Latest Covid-19 India Status.csv")
    # data=pd.read_csv("https://raw.githubusercontent.com/Rjchauhan18/Competition/main/Latest%20Covid-19%20India%20Status.csv")

    data.rename(columns={"State/UTs": "State"},inplace=True)
    st.title("India Covid-19 Data")
    st.table(data)
    # st.write(data)
    fig = px.line(data, x="State", y="Death Ratio", title="Death Ratio by State")
    fig.update_layout(title = { 'font' : { 'size' : 25}})
    fig.update_traces(line=dict(color='red'))
    fig.update_layout(height = 500, width = 1000)
    fig.layout.update( xaxis_rangeslider_visible=True, xaxis_rangeslider_thickness = 0.05)
    st.plotly_chart(fig, use_container_width=False, use_container_height=False)
    
    # data_dict = data.to_dict()
    # print(data_dict)
    # st.plotly_chart(d)
    def Graph_of_Discharge_Ratio():
        fig = go.Figure()
        fig.add_trace(go.Scatter( x=data['State'], y=data['Discharge Ratio'], name="States"))
        fig.add_trace(go.Scatter(x=data['State'], y=data['Discharge Ratio'], name="Discharge Ratio"))
        fig.update_layout(title = { 'font' : { 'size' : 25}})
        fig.layout.update(
            title_text='Discharge Ratio by State', xaxis_rangeslider_visible=True, xaxis_rangeslider_thickness = 0.05)
        fig.update_layout(height = 500, width = 1000)
        fig.update_traces(line=dict(color='red'))
        st.plotly_chart(fig , use_container_width=False, use_container_height=False)
    Graph_of_Discharge_Ratio()
    
    def Graph_of_Total_Cases():
        fig = go.Figure()
        fig.add_trace(go.Scatter( x=data['State'], y=data['Total Cases'], name="States"))
        fig.add_trace(go.Scatter(x=data['State'], y=data['Total Cases'], name="Total Cases"))
        fig.layout.update(
            title_text='Total cases by State', xaxis_rangeslider_visible=True, xaxis_rangeslider_thickness = 0.05)
        fig.update_layout(title = { 'font' : { 'size' : 25}})
        fig.update_layout(height = 500, width = 1000)    
        fig.update_traces(line=dict(color='red'))
        st.plotly_chart(fig , use_container_width=False, use_container_height=False)
    Graph_of_Total_Cases()
    
# app() 




def SignUp():
    with st.form(key="SignUp"):
        user=st.text_input("Enter Your Username")
        Fullname=st.text_input("Enter Your Full name")
        email=st.text_input("Enter Your Email ID")
        password=st.text_input("Enter Your Password",type="password")
        re_password=st.text_input("Re-Enter Your Password",type="password")

       
        if st.form_submit_button("Submit"):
            if password==re_password:
                e=db.check(email)
                if e=="Valid Email":
                    if db.get_user(user) != None:
                        st.warning("Username already in Exist !!!")
                    else:
                        if len(user) >3:
                            if len(password) >6:
                                # Hashed_password = stauth.Hasher([password]).generate()
                                db.insert_user(user,Fullname,email,password)
                                st.success("Account successfully Created !!!")
                                st.balloons()
                            else:
                                st.warning("Password should be at least 6 characters")
                        else:
                            st.warning("Username is too short")   
                else:
                    st.warning("Invalid Email ID")
            else:
                st.error("Password does not match")

def Login():

    with st.form(key="Login"):
        username= st.text_input( 'Username')
        password= st.text_input('Password',type='password')

        if st.form_submit_button('Login'):
            try:
                loggedIn_user=db.get_user(username)

            except:
                pass

            if loggedIn_user !=None:
                
                if loggedIn_user["Password"] == password:
                    st.session_state.status=True
                    st.session_state.un=loggedIn_user["key"]

                    st.info("You have successfully logged In")
                    # st.stop()
                    st.experimental_rerun()
                else:
                    st.error("Incorrect Password")
                
            else:
                st.error("Invalid Username")



# Login / SignUp setup with session state
status=None
                      
if 'status' not in st.session_state:
    st.session_state.status=status


if st.session_state.status==False or st.session_state.status==None:
    col1,col2,col3=st.columns([1.3,2,3/2])
    with col2:
        st.title('WELCOME TO STOCK PORTFOLIO APP')

        login,signup=st.tabs(["Login", "SignUp"])

        with login:
            Login()
                        
        with signup:
            SignUp()


elif st.session_state.get('status')==True:
            # st.header(st.session_state.get('un'))
            app(st.session_state.get('un'))

# lottie_url_hello = "https://lottie.host/5a63af3e-04ef-4ee5-84c5-ce1df73fdbd1/bhK1pYQOhv.json"

# lottie_hello = load_lottieurl(lottie_url_hello)




# loginContainer = st.container()
# with loginContainer:
#     column1,column2=st.columns(2)
#     with column1:
        

#         st_lottie(lottie_hello, key="login")
#     with column2:
        



# conn = st.experimental_connection('mysql', type='sql')

# loggedIn_user=None

# # def signal():
# #     return loggedIn_user

# if 'loggedIn_user' not in st.session_state:
#     st.session_state.loggedIn_user=loggedIn_user



        
# if st.session_state.get("loggedIn_user") == True:
#     app()

# if st.session_state.get("loggedIn_user") == False or st.session_state.get("loggedIn_user") == None:
#     st.title("COVID-19 MANAGEMENT SYSTEM")
    
#     choice = st.selectbox('Login/SignUp',['Login', 'SignUp'])
#     if choice == 'Login':
            
#         Full_name= st.text_input( 'Full_name ')
#         email= st.text_input('Email id')
#         password= st.text_input('Enter Your Password',type="password")

    
#         if st.button('Login'):
#             try:
#                 detail,loggedIn_user=db.fetch_user(Full_name, email,password)
#             except:
#                 pass

#             if loggedIn_user == True:
#                 st.session_state["loggedIn_user"]=loggedIn_user
#                 st.info("You have successfully logged In")
#                 # st.stop()
#                 st.experimental_rerun()
                
#             elif loggedIn_user == "Invalid Email ID":
#                 st.error("Invalid Email ID")
            
#             else:
#                 st.session_state["loggedIn_user"]=loggedIn_user
                
#                 st.error("Invalid Patient Detail")
#                 st.warning("Log In failed")
    


#     else:
#         Full_name= st.text_input('Enter Your Full Name')
#         # lt_name= st.text_input('Last Name')
#         email= st.text_input('Email ID')
#         age= st.text_input('Enter your age')
#         phone= st.text_input('Enter Your Phone Number ')
#         password= st.text_input('Enter Your Password ', type="password")
#         Re_enter= st.text_input('Re-enter your password', type="password")

#         if st.button('Create My Account'):
#         #   user = auth.create_user( email=email, password=password,uid=username)
#             if password==Re_enter:

#                 created_user=db.create_user(Full_name,email,age,phone,password)
#                 if created_user == True:
#                     st.balloons()

#                     st.write('Sucessfully created Account')
#                 else:
#                     st.write(created_user)
#                     st.warning('Account creation failed')
#             else:
#                 st.warning("Passowrds Doesn't Match")
                
                
                
        
