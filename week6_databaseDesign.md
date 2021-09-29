# Python with CSV files

[YouTube - Socratica - CSV Files in Python](https://www.youtube.com/watch?v=Xi52tx6phRU)

### Taking command-line arguments

```python3
import sys
...
if len(argv) >= 3: # ensure there are at least two arguments
  ...
else:
  print("Usage: ...")
```

`argv` is a list, where `argv[0]` is the name of the program being run, `argv[1]` is the first argument, etc

### Working with Lists

```python3
mylist = ['asdf', 'qwer', 'poiu'] # defining a list
print(mylist[0]) # print item at index zero, 'asdf' in this case
print(len(mylist)) # get the length of the list
mylist.append(4) # append a single item to the list
mylist2 = ['a', 'b', 'c']
mylist.extend(mylist2) # append all the items from mylist2 to mylist
```

### Working with Files and CSV

```python3
import csv

# open a file for reading
with open ("myfile.csv", 'r') as inputfile:
  reader = csv.reader(inputfile)
  for line in reader: # reads all the lines from the csv file, one at a time
    ...               # 'line' is a list of the cells in the csv file
    
# open a file for writing
with open ("outputfile.csv", 'w') as outputfile:
  writer = csv.writer(outputfile)
  writer.writerows(list_of_lists) # output a 2d list to the file all-at-once
  .. or ..
  writer.writerow(mylist) # output a list as a single line to the file
```

### Ensuring the Script is Run Directly

```python3
if __name__ == "__main__":
  .. # this will run if the script is called directly
else:
  .. # this will run if it is imported as a module, typically nothing is done here
```

## Code outline for splitting on a cell

```python3
open your input and output files:
  parse the inputfile with a csv.reader
  for line in inputfile:
    targetCell = line[col_num]
    line.extend(targetCell.split(delimiter))
    line.pop(col_num) # remove the original row
    possibly add some blank cells to the other rows so that all rows have the same number of cells
    write the row to the output file with csv.writer
```

### Code outline for creating a bridging table

```python3
open your input and output files:
  parse the inputfile with a csv.reader
  for line in inputfile:
    targetCell = line[col_num]
    multi_values_list = targetCell.split(delimieter)
    for each value in the the multi_values_list
      output to the output file the two keys (the primary key of the input table), and this value
```

# The Entity-relationship model

## 4.1 Entities, relationships, and attributes

[YouTube - Gina Baldazzi - ERD Training Video - 15:03](https://www.youtube.com/watch?v=-fQ-bRllhXc)

An entity-relationship model includes three kinds of objects:

- **Entity**
- **Relationship**
- **Attribute**

An **ER diagram**, is a schematic picture of entities, relationships, and attributes. It describes the interrelation of things of interest (the entities)

### Types and instances

In entity-relationship modeling, a type is a set:

- An entity type is a set of things. Ex: All employees in a company.
- A relationship type is a statement about entity types. Ex: Employee-Manages-Department. 
- An attribute type is a set of values. Ex: All employee salaries. 

Entity, relationship, and attribute types usually become tables, foreign keys, and columns, respectively.

An instance is an element of a set:

- An entity instance is an individual thing. Ex: The employee Sam Snead.
-  A relationship instance is a statement about entity instances. Ex: "Maria Rodriguez manages Sales."
- An attribute instance is an individual value. Ex: The salary $35,000.

### Database design

Complex databases are developed in three phases: 

1. Analysis develops an entity-relationship model, capturing data requirements while ignoring implementation details.

   | Step | Name                                             |
   | ---- | ------------------------------------------------ |
   | 1    | Discover entities, relationships, and attributes |
   | 2    | Determine cardinality                            |
   | 3    | Distinguish independent and dependent entities   |
   | 4    | Create supertype and subtype entities            |

2. Logical design converts the entity-relationship model into tables, columns, and keys for a particular database system.

   | Step | Name                    |
   | ---- | ----------------------- |
   | 5    | Implement entities      |
   | 6    | Implement relationships |
   | 7    | Implement attributes    |
   | 8    | Normalize tables        |

3. Physical design adds indexes and specifies how tables are organized on storage media.

## 4.2 Discovery

Entities - these usually appear as nouns, but not all nouns are entities. Focus on those relevant to database

Relationships - often expressed as verbs. We only need the ones that are about entities

Attributes - usually nouns that denote specific data such as names, dates, dollar amounts, etc

Entity names should be a singular noun - Example: Student (not Students). These names should be easy to understand and commonly used

Relationship names should be active rather than passive - Example: Student takes Course (Not course taken by student)

Attributes have the form EntityQualifierType - StudentPhoneNumber (not PhoneStudent, or such)

Avoid synonyms (Don't switch between calling someone a student and a trainee)

## 4.3 Cardinality

Maxima and minima usually depend on business rules

### Relationship cardinality

Relationship maximum is the greatest number of instances of one entity that can relate to a single instance of another entity - this is usually either 1 or 'many', but sometimes a specific number

Relationship minimum is the least number of instances of one entity that can relate to a single instance of another entity - this is usually either 1 or 0. 

Maxima are shown outside parentheses, minima are shown in parentheses

Passenger 1(1) ------ M(1)   Booking   M(0) ----- 1(1) Flight

### Attribute cardinality

- Singular attribute — each entity instance has at most one attribute instance.
- Plural attribute — each entity instance can have many attribute instances.
- Unique attribute — each attribute instance describes at most one entity instance.

In ER diagrams, Unique?-max (min)

EmployeeNumber 1-1(1)  (unique - singular, min 1)
PassportNumber 1-M(0) (unique - plural, min 0)
FullName M-1 (not unique - singular)
SkillCode M-M (not unique - plural)

Attribute Minima appear in parenthese after this

## 4.4 Independent and dependent entities

A **dependent entity** depends on a another entity, called the **master entity**

Subtask -> Task -> Project

ER diagram design varies significantly, but it is usually just a matter of style

Need examples of dependencies

## 4.5 Supertype and subtype entities

[YouTube - Appficial - IsA Relationship (2:46)](https://www.youtube.com/watch?v=s9N2EDYdlC0)

Example: managers are a subset of employees, so Manager is a subtype entity of the Employee supertype

In ER diagrams, supertypes are drawn as a box around the subtypes

The dependency relationship from subtype to supertype is called an IsA relationship - Manager-IsAn-Employee

Similar entities can become subtypes of a common supertype - Student, Faculty, and Staff can all be subtypes of Person

An entity with many optional attributes also suggests a new supertype and subtype entities

A **partition** of a supertype is a group of mutually exclusive subtype entities - example: undergraduate vs graduate students. A **partition attribute** specifies to which partition they belong

​	There can be multiple partitions that divide the supertype differently (Undergrad vs grad, married vs nonmarried)

## 4.6 Implementing entities

Attributes of a primary key

* Unique
* Required (non-null)
* Stable - They should not change. Changes to a primary key would require cascading to foreign keys
* Simple - Easy to store. Easy to specify in 'where' statements and speed up query processing
* Meaningless - This helps them be more stable and simple

Independent entities

Walk through examples of entities and choosing keys

[YouTube - LucidChard - Entity Relationship Diagram - 6:57](https://www.youtube.com/watch?v=QpdhBUYk7Kk)

