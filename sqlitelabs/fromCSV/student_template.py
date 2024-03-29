import csv
import my_interface

def read_speakers_csv(conn):
    """
    Read from 'speaker.csv' file and insert them into the Speaker table
    :param conn:
    :return number of entries inserted:
    """
    numentries = 0
    # Insert your code here
    
    return numentries


def read_speaker_category_csv(conn):
    """
    Read from 'speaker_category.csv' file and insert them into the Speaker table
    :param conn:
    :return number of entries inserted:
    """
    numentries = 0
    # Insert your code here
    
    return numentries


def read_category_csv(conn):
    """
    Read from 'category.csv' file and insert them into the Speaker table
    :param conn:
    :return number of entries inserted:
    """
    # Insert your code here
    
    return numentries

if __name__ == '__main__':

    # Create connection to sqlite in-memroy database
    conn = my_interface.create_connection()
    if conn is None:
        print("Error! cannot create the database connection.")

    # Create tables
    my_interface.create_speaker_table(conn)
    my_interface.create_category_table(conn)
    my_interface.create_speaker_category_table(conn)

    # Insert row to Horse table
    read_speakers_csv(conn)
    read_category_csv(conn)
    read_speaker_category_csv(conn)

    # Selecting the rows from all three tables
    print("Selecting * from speaker")
    print(my_interface.select_all_speakers(conn))
    print("Selecting * from speaker_category")
    print(my_interface.select_all_speaker_category(conn))
    print("Selecting * from Category")
    print(my_interface.select_all_categories(conn))


