import sqlite3
myconnection = sqlite3.connect("mytest.db")
mycursor = myconnection.cursor()
myrows = mycursor.execute("select * from mytest;")
for row in myrows:
    print(row)



mycursor.close()
myconnection.close()
