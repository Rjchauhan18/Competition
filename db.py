import os
import mysql.connector 
import datetime as dt
import pandas as pd
from dotenv import load_dotenv

load_dotenv(".env")
user_name=os.getenv("user_name")
password=os.getenv("password")

mydb = mysql.connector.connect(
    # host="127.0.0.1",
    host="localhost",
    port="3306",
    user=user_name,
    password=password,
    database="competition"
)
# print(mydb)

mycursor = mydb.cursor(dictionary=True)
# import csv

# def import_csv_data(filename):
#     with open(filename, "r") as csvfile:
#         reader = csv.DictReader(csvfile)
#         # r=parse_csv_to_json(reader)
#         # st.write(r[0]) 
#         staff_list = []
#         for row in reader:
#             staff_list.append((row["id"], row["name"],row["Hospital name"], row["Contact"], row["Field"], row["Avilible"]))
#     return staff_list

# s=import_csv_data('pages\staff_management.csv')
# print(s)

# mycursor.execute("CREATE TABLE staff_manage (id VARCHAR(25), name VARCHAR(150),Hospital_name VARCHAR(300),Contact VARCHAR(10),Field varchar(80),Availible varchar(10))")

def ins(id,name,Hospital_name,Contact,Field,Availible):
    try:

            sql = " INSERT INTO staff_manage(id,name,Hospital_name,Contact,Field,Availible) VALUES(%s,%s,%s,%s,%s,%s)"
            value=(id,name,Hospital_name,Contact,Field,Availible)
            mycursor.execute(sql,value)
            mydb.commit()
            return True
    except Exception as e:
                return e
# print(s[0][0])
# for l in s:
#         print(ins(l[0],l[1],l[2],l[3],l[4],l[5]))
     
     
def fetchuing_Staff(Hospital_name):
    try:
        sql = "SELECT * FROM staff_manage WHERE Hospital_name = %s "
        detail = (Hospital_name,)
        

        mycursor.execute(sql, detail)
        user_detail = mycursor.fetchall()
        return user_detail

    except Exception as e:
         pass
        # print(e)
        # return "Invalid Patient detail"

# fetchuing_Staff("Nationwide Laboratories, LLC")

"""
fetching all the user 
"""
def fetch_users():
    mycursor.execute("SELECT * FROM users")

    rows = mycursor.fetchall()
    print(rows[0])
# fetch_users()
# fetch the one single user

"""
Fetching the detail Of existing particular users detail
"""
def fetch_user(name,Email_id,password):
    try:
        sql = "SELECT * FROM users WHERE email = %s "
        detail = (Email_id,)
        

        mycursor.execute(sql, detail)
        print("!")
        user_detail = mycursor.fetchall()

    except Exception as e:
        print(e)
        return "Invalid Patient detail"


    nm=user_detail[0]["full_name"]
    pw=user_detail[0]["password"]
 
    if name == nm :
        
        if password== pw:
            return user_detail,True
        else:
            return False
    else:
        return "Incorrect Name"
""" 
Creating User with mysql
"""
def create_user(full_name,email,age,phone,password):
    try:

        sql = " INSERT INTO users(full_name,email,age,phone,password) VALUES(%s,%s,%s,%s,%s)"
        value=(full_name,email,age,phone,password)
        mycursor.execute(sql,value)
        mydb.commit()
        return True
    except Exception as e:
            return e
# r=create_user("Nohan Thomas","NOhan@gmail.com",20,9724382108)
# print(r)