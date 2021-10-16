import mysql.connector
import sys


try:
    import dbconnect
    mydb = dbconnect.mydb
except:
    print(
"""Error: Couldn't read the credentials to connect to the database. Create dbconnect.py

Example:

mydb = mysql.connector.connect(
  host="127.0.0.1",
  port="3306",
  user="jeff",
  password="mypass",
  database="sakila"
)

Also, be sure not to track this file with git by adding it to your .gitignore file
""")
    sys.exit()


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

mycursor.close()
mydb.close()
