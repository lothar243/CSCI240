There are three sql files whose data needs to be added to the database - speaker.csv, speaker-category.csv, and category.csv. Each of these have the first row used for column headers. If you need more information about these tables or spreadsheets, this is listed below.

There are already functions for inserting the data.

* my_interface.insert_speaker(conn, row)
* my_interface.insert_category(conn, row)
* my_interface.insert_speaker_category(conn, row)

For each of these, conn is a connection object, passed in as a parameter. row is a list of each of the cells for a particular row

You will need to open each of these files, and I recommend using the csv module. Use the built-in help files or the information on Moodle (or an internet search) for more information on how to use this module.

---

# Additional Information

The column headers and the corresponding tables are as follows.

### Speakers

speaker.csv: Guest ID, First Name, Last Name, Short Description, Bio, Current Image, Image Width, Image Height, Current Logo, Logo, Width, Logo Height, Web Address

```sql
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
);
```

### Speaker_category

speaker_category.csv: Guest ID, Category ID

```sql
CREATE TABLE Speaker_category (
  Guest_id integer NOT NULL,
  Category_id integer NOT NULL,
  PRIMARY KEY (Guest_id, Category_id)
);
```

### Category

category.csv: Category ID, Category

```sql
CREATE TABLE Category (
  Category_id integer PRIMARY KEY NOT NULL,
  Category text
);
```


Tables have already been created with names that match the column headers and appropriate data types (text for all except IDs, Width, and Height)
