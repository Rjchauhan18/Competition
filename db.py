import mysql.connector , secret
import mysql
import datetime as dt
import pandas as pd


mydb = mysql.connector.connect(
#   host="localhost",
    host="192.168.1.100",

    user=secret.user_name,
    password=secret.password,
    database="competition"
)

# print(mydb)

mycursor = mydb.cursor(dictionary=True)



# mycursor.execute("CREATE TABLE users (full_name VARCHAR(255), email VARCHAR(150),age VARCHAR(3),phone VARCHAR(10),password varchar(8))")

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
s=fetch_user("Jagdish Chauhan","jn@gmail.com","Jn@1971")
print(s)


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