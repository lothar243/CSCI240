import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    port="23306",
    user="jeff",
    password="mypass"
)

print(mydb)
