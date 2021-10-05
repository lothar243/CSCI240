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

myresult = mycursor.fetchall()

print("***** Examining the objects we have *****")
print(f"{mycursor=}")
print(f"{myresult=}")
print("*****************************************")

print()
print("This is what the results look like when we print them one line at a time:")
print(mycursor.column_names)
for x in myresult:
    print(x)
