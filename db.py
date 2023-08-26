import mysql.connector , config
import mysql
import yfinance as yf
import datetime as dt
import pandas as pd
# import jwt
# pyload_data= {
#      "sub": "4242",
#      "name": "Rahul Chauhan",
#      "nickname": "Rjchauhan"
# }


# my_secret = 'my_super_secret'
# token= jwt.encode(
#     payload=pyload_data,
#     key=my_secret
# )

# # print(token)















# import requests module
# # set username and password
# s.auth = ('user', 'pass')
 
# # update headers
# s.headers.update({'x-test': 'true'})
 
# # both 'x-test' and 'x-test2' are sent
# s.get('https://httpbin.org / headers', headers ={'x-test2': 'true'})
 
# # print object
# print(s)
mydb = mysql.connector.connect(
  host="localhost",
  user=config.user_name,
  password=config.password,
  database="competition"
)

# print(mydb)

mycursor = mydb.cursor(dictionary=True)



# mycursor.execute("CREATE TABLE users (full_name VARCHAR(255), email VARCHAR(150),age VARCHAR(3),phone VARCHAR(10))")

# fetch all the user 
def fetch_users():
    mycursor.execute("SELECT * FROM users")

    rows = mycursor.fetchall()
    print(rows[0])
# fetch_users()
# fetch the one single user
def fetch_user(name,Email_id):
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
 
    if name == nm:
        return True
    else:
        return False
s=fetch_user("Rahul Chauhan","rjchauhan@5000000gmail.com")
print(s)

def create_user(full_name,email,age,phone):
    try:

        sql = " INSERT INTO users(full_name,email,age,phone) VALUES(%s,%s,%s,%s)"
        value=(full_name,email,age,phone)
        mycursor.execute(sql,value)
        mydb.commit()
        return True
    except Exception as e:
            return e
# r=create_user("Nohan Thomas","NOhan@gmail.com",20,9724382108)
# print(r)