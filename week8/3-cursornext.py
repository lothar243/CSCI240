import sqlite3

conn = sqlite3.connect("speakers.db")
mycursor = conn.cursor()

mycursor.execute("select * from Speaker limit 10;")


print("here's the output fetching it one line at a time")
# print(mycursor.column_names)
column_names = [column[0] for column in mycursor.description]
print(column_names)
row = mycursor.fetchone()
while row is not None:
    print(row)
    row = mycursor.fetchone()

mycursor.close()
conn.close()
