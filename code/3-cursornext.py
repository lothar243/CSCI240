import mysql.connector
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


print("here's the output fetching it one line at a time")
print(mycursor.column_names)
myresult = mycursor.fetchone()
while myresult is not None:
    print(myresult)
    myresult = mycursor.fetchone()

mycursor.close()
mydb.close()
