import sqlite3
from sqlite3 import Error

# Create a connection to sqlite in-memory database
def create_connection():
    """ 
    Create a connection to in-memory database 
    :return: Connection object
    """
    
    try:
        conn = sqlite3.connect(":memory:")
        return conn
    except Error as e:
        print(e)

    return None

# Create Horse table
def create_table(conn):
    """ 
    Create Horse table
    :param conn: Connection object
    :return:
    """
    sql_create_horse_table = """ 
        CREATE TABLE Horse (
            Id integer PRIMARY KEY NOT NULL,
            Name text,
            Breed text,
            Height double,
            BirthDate text
         ); """

    try:
        c = conn.cursor()
        c.execute(sql_create_horse_table)
    except Error as e:
        print(e)

# Inserts data as a row in Horse table using paramenters
# Note sqlite placeholder character is ?
def insert_horse(conn, data):
    """
    Create a new row in Horse table
    :param conn:
    :param data:
    :return: horse id
    """
    sql = "INSERT INTO Horse VALUES(?, ?, ?, ?, ?)"
    cur = conn.cursor()
    cur.execute(sql, data)


# Selects and prints all rows of Horse table
def select_all_horses(conn):
    """
    Query all rows in the Horse table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Horse")

    rows = cur.fetchall()

    for row in rows:
        print(row)
    

if __name__ == '__main__':

    # Create connection to sqlite in-memroy database
    conn = create_connection()
    if conn is None:
        print("Error! cannot create the database connection.")

    # Create Horse table
    create_table(conn)
    
    # Insert row to Horse table
    horse_data = (1, "Babe", "Quarter Horse", 15.3, "2015-02-10")
    insert_horse(conn, horse_data)

    # Select and print all Horse table rows
    print("All horses:")
    select_all_horses(conn)

