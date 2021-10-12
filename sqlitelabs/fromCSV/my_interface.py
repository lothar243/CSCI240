import csv
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

# Create Speaker table
def create_speaker_table(conn):
    """
    Create Speaker table
    :param conn: Connection object
    :return:
    """
    sql_create_speaker_table = """
        CREATE TABLE Speaker (
            Guest_id integer PRIMARY KEY NOT NULL,
            First_name text,
            Last_name text,
            Short_description text,
            Bio text,
            Current_image text,
            Image_width integer,
            Image_height integer,
            Current_logo text,
            Logo_width integer,
            Logo_height integer,
            Web_address text
         ); """

    try:
        c = conn.cursor()
        c.execute(sql_create_speaker_table)
    except Error as e:
        print(e)

# Create speaker-category table
def create_speaker_category_table(conn):
    """
    Create speaker_category table
    :param conn: Connection object
    :return:
    """
    sql_create_speaker_category_table = """
        CREATE TABLE Speaker_category (
            Guest_id integer NOT NULL,
            Category_id integer NOT NULL,
            PRIMARY KEY (Guest_id, Category_id)
         ); """

    try:
        c = conn.cursor()
        c.execute("drop table if exists Speaker_category;")
        c.execute(sql_create_speaker_category_table)
    except Error as e:
        print(e)

# Create speaker-category table
def create_category_table(conn):
    """
    Create category table
    :param conn: Connection object
    :return:
    """
    sql_create_category_table = """
        CREATE TABLE Category (
            Category_id integer PRIMARY KEY NOT NULL,
            Category text
         ); """

    try:
        c = conn.cursor()
        c.execute(sql_create_category_table)
    except Error as e:
        print(e)

# Inserts data as a row in Speaker table using paramenters
# Note sqlite placeholder character is ?
def insert_speaker(conn, data):
    """
    Create a new row in Speaker table
    :param conn:
    :param data:
    :return: speaker id
    """
    sql = "INSERT INTO Speaker VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cur = conn.cursor()
    cur.execute(sql, data)


# Inserts data as a row in Speaker table using paramenters
# Note sqlite placeholder character is ?
def insert_category(conn, data):
    """
    Create a new row in Category table
    :param conn:
    :param data:
    :return: category id
    """
    sql = "INSERT INTO Category VALUES(?, ?)"
    cur = conn.cursor()
    cur.execute(sql, data)


# Inserts data as a row in Speaker table using paramenters
# Note sqlite placeholder character is ?
def insert_speaker_category(conn, data):
    """
    Create a new row in Speaker_category table
    :param conn:
    :param data:
    :return: category id
    """
    sql = "INSERT INTO Speaker_category VALUES(?, ?)"
    cur = conn.cursor()
    cur.execute(sql, data)


# Read rows from speaker.sql and insert them into the Speaker table
def read_speakers(conn):
    """
    Read from 'speaker.csv' file
    :param conn:
    :return number of entries inserted:
    """
    numentries = 0
    with open ("speaker.csv", "r") as csvfile:
        # discard the first row
        csvfile.readline()

        reader = csv.reader(csvfile)
        for row in reader:
            insert_speaker(conn, row)
            numentries += 1
    return numentries


# Read rows from speaker.sql and insert them into the Speaker table
def read_speaker_category(conn):
    """
    Read from 'speaker_category.csv' file
    :param conn:
    :return number of entries inserted:
    """
    numentries = 0
    with open ("speaker_category.csv", "r") as csvfile:
        # discard the first row
        csvfile.readline()

        reader = csv.reader(csvfile)
        for row in reader:
            insert_speaker_category(conn, row)
            numentries += 1
    return numentries


# Read rows from speaker.sql and insert them into the Speaker table
def read_category(conn):
    """
    Read from 'category.csv' file
    :param conn:
    :return number of entries inserted:
    """
    numentries = 0
    with open ("category.csv", "r") as csvfile:
        # discard the first row
        csvfile.readline()

        reader = csv.reader(csvfile)
        for row in reader:
            insert_category(conn, row)
            numentries += 1
    return numentries

# Selects and prints all rows of Speaker table
def select_all_speakers(conn):
    """
    Query all rows in the Speaker table
    :param conn: the Connection object
    :return output string:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Speaker")

    rows = cur.fetchall()

    for row in rows:
        print(row)


# Selects and prints all rows of Speaker table
def select_all_categories(conn):
    """
    Query all rows in the Category table
    :param conn: the Connection object
    :return output string:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Category")

    rows = cur.fetchall()

    for row in rows:
        print(row)


# Selects and prints all rows of Speaker table
def select_all_speaker_category(conn):
    """
    Query all rows in the Speaker_category table
    :param conn: the Connection object
    :return output string:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Speaker_category")

    rows = cur.fetchall()

    for row in rows:
        print(row)
