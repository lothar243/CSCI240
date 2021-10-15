import sqlite3

# Create a connection to the sqlite DBMS
conn = sqlite3.connect("speakers.db")
# conn = sqlite3.connect(":memory:")

# Verify that we have a connection
print(conn)
conn.close()
