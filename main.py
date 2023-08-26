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
        st.experimental_rerun("")

    data=pd.read_csv("Latest Covid-19 India Status.csv")
    st.write(data.keys())
    data.rename(columns={"State/UTs": "State"},inplace=True)
    st.write(data)
    st.line_chart(data,x="State",y="Discharge Ratio",height=275,width=200)
    
    # data_dict = data.to_dict()
    # print(data_dict)
    # st.plotly_chart(d)
    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter( x=data['State'], y=data['Discharge Ratio'], name="States"))
        fig.add_trace(go.Scatter(x=data['State'], y=data['Discharge Ratio'], name="Discharge Ratio"))
        fig.layout.update(
            title_text='Covid-19 State data', xaxis_rangeslider_visible=True)
        height = 500
        width = 800
        st.plotly_chart(fig ,height=height, width=width, use_container_width=True)
    plot_raw_data()
    def get_chart(data):
        hover = alt.selection_single(
            fields=["date"],
            nearest=True,
            on="mouseover",
            empty="none",
        )

        lines = (
            alt.Chart(data, title="Evolution of stock prices")
            .mark_line()
            .encode(
                x="date",
                y="price",
                color="symbol",
            )
        )

        # Draw points on the line, and highlight based on selection
        points = lines.transform_filter(hover).mark_circle(size=65)

        # Draw a rule at the location of the selection
        tooltips = (
            alt.Chart(data)
            .mark_rule()
            .encode(
                x="yearmonthdate(date)",
                y="price",
                opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
                tooltip=[
                    alt.Tooltip("date", title="Date"),
                    alt.Tooltip("price", title="Price (USD)"),
                ],
            )
            .add_selection(hover)
        )
        return (lines + points + tooltips).interactive()
    def alter():
        # from vega_datasets import data

        # @st.experimental_memo
        # def get_data():
        #     source = data.stocks()
        #     source = source[source.date.gt("2004-01-01")]
        #     return source

        # source = get_data()

        # # Original time series chart. Omitted `get_chart` for clarity
        # chart = get_chart(source)

        # Input annotations
        ANNOTATIONS = [
            ("Mar 01, 2008", "Pretty good day for GOOG"),
            ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"),
            ("Nov 01, 2008", "Market starts again thanks to..."),
            ("Dec 01, 2009", "Small crash for GOOG after..."),
        ]

        # Create a chart with annotations
        annotations_df = pd.DataFrame(ANNOTATIONS, columns=["State", "Discharge Ratio"])
        # annotations_df.date = pd.to_datetime(annotations_df.date)
        chart= data["Discharge Ratio"]
        annotations_df["y"] = 0
        annotation_layer = (
            alt.Chart(annotations_df)
            .mark_text(size=15, text="⬇", dx=0, dy=-10, align="center")
            .encode(
                x="date:T",
                y=alt.Y("y:Q"),
                tooltip=["event"],
            )
            .interactive()
        )

        # Display both charts together
        st.altair_chart((chart + annotation_layer).interactive(), use_container_width=True)


app()



# st.title("COVIED-19 MANAGEMENT SYSTEM")
# st.write("---")


# loggedIn_user=None

# if 'loggedIn_user' not in st.session_state:
#     st.session_state.loggedIn_user=loggedIn_user


        

# if st.session_state.get("loggedIn_user") == True:
#     app()

# if st.session_state.get("loggedIn_user") == False or st.session_state.get("loggedIn_user") == None:
    
#     choice = st.selectbox('Login/SignUp',['Login', 'SignUp'])
#     if choice == 'Login':
        
#         Full_name= st.text_input( 'Full_name ')
#         email= st.text_input('Email id')
#         password= st.text_input('Enter Your Password',type="password")

    
#         if st.button('Login'):
#             try:
#                 loggedIn_user=db.fetch_user(Full_name, email,password)
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
                
                
                
        
