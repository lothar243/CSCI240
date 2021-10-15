import sqlite3
import sys

conn = sqlite3.connect("speakers.db")


mycursor = conn.cursor()

mycursor.execute("select first_name, last_name, Web_address from speaker limit 10;")

myresult = mycursor.fetchall()

print("***** Examining the objects we have *****")
print(f"{mycursor=}")
print(f"{myresult=}")
print("*****************************************")

print()
print("You can get the column names by looking at the mycursor.description")
for colInfo in mycursor.description:
    print(colInfo[0])
print()
print("This is what the results look like when we print them one line at a time:")
for x in myresult:
    print(x)

mycursor.close()
conn.close()
