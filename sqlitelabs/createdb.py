import sqlite3
myconnection = sqlite3.connect("mytest.db")
mycursor = myconnection.cursor()

mycursor.execute("drop table if exists mytest")
mycursor.execute("create table mytest (id integer primary key, name text);")
myresult = mycursor.execute("insert into mytest values (1, 'asdf');")
print(myresult.description)
mycursor.execute("insert into mytest values (2, 'aidf');")

mycursor.close()
myconnection.commit()
myconnection.close()
