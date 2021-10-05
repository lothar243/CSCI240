import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    port="23306",
    user="jeff",
    password="mypass",
    database="sakila"
)

mycursor = mydb.cursor()

mycursor.execute("select * from actor limit 10;")


print("here's the output fetching it one line at a time")
print(mycursor.column_names)
myresult = mycursor.fetchone()
while myresult is not None:
    print(myresult)
    myresult = mycursor.fetchone()
