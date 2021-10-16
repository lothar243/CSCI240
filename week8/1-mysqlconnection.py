# if you haven't already, you need to: pip3 install mysql-connector-python
import mysql.connector

# Create a connection to the mySQL DBMS
# By default, mySQL uses port 3306.
# This connection info should not be uploaded to GitHub normally. Instead, you could import another file that contains only the connection info and is not part of the git repository.
conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="jeff",
    password="mypass"
)

# Verify that we have a connection
print(conn)
conn.close()
