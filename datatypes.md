# Data types

## Simple Data Types

Integer, Decimal, Character, Time, Binary, Semantic

## Complex Types

* Collection - for example sets and arrays
* Document - XML and JSON
* Spatial - Geometric information
* Object - Object-oriented constructs

## Collection types

* Set

```sql
CREATE TABLE Employee (
   ID INTEGER,
   Name VARCHAR(20),
   Language SET('English', 'French', 'Spanish', 'Mandarin', 'Japanese'),
   PRIMARY KEY (ID)
);
```

With sets, order is not important and there is no repetition, so data can be significantly compressed - with a single bit per option.

* Multiset - values can be repeated but are not ordered
* List - values can be repeated and are ordered
* Array - adds an index to a list, can be multidimensional

In PostgreSQL

```
CREATE TABLE Employee (
  ID INTEGER,
  Name VARCHAR(20),
  QuarterlySales INTEGER[4],
  PRIMARY KEY (ID)
);

INSERT INTO Employee (ID, Name, QuarterlySales)
VALUES (2538, 'Lisa Ellison', '{ 1450, 2020, 900, 5370 }'),
       (6381, 'Maria Rodriguez', '{ 3340, 800, 1700, 6400 }'),
       (7920, 'Jiho Chen', '{ 0, 3900, 8000, 320 }');
```

## Document Types

* Structured data - Fixed set of named data elements, organized in groups
* Semistructured data - Each group may have a different number of elements with different names
* Unstructured data - Raw text. Element names are not declared

Semistructured data is typically stored in a document using a format like XML or JSON

### XML

eXtensible Markup Language

* Similar to HTML (Uses tags with brackets < and >)
* Data is untyped
* Hierarchical through nesting

### JSON

JavaScript Object Notation

* Looks similar to printing collections in Python (except for true, false, null)
* Data is typed (String, Number, Boolean, Null, Array, Object)
* Hierarchical through nesting

XML vs JSON

* JSON is more popular
* XML came first (around 1990), but the file sizes are larger
* Security problems because of (XML external entity injection, see XXE)

