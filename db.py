import mysql.connector , config
import mysql
import datetime as dt
import pandas as pd


mydb = mysql.connector.connect(
  host="localhost",
  user=config.user_name,
  password=config.password,
  database="competition"
)

# print(mydb)

mycursor = mydb.cursor(dictionary=True)



# mycursor.execute("CREATE TABLE users (full_name VARCHAR(255), email VARCHAR(150),age VARCHAR(3),phone VARCHAR(10),password varchar(8))")

# fetch all the user 
def fetch_users():
    mycursor.execute("SELECT * FROM users")

    rows = mycursor.fetchall()
    print(rows[0])
# fetch_users()
# fetch the one single user
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
            return True
        else:
            return False
    else:
        return "User name Incorrect"
# s=fetch_user("Rahul Chauhan","rjchauhan@5000000gmail.com")
# print(s)

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