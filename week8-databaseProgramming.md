# Programming Languages

## Imperative languages

* The programmer explicitly controls the flow of the execution
* Can be procedural, like C, Cobol
* Can be object-oriented like Java, Python, and C++

## Declarative languages

* Use an optimizer to determine the specific execution path
* Example: SQL

Complete applications often need both explicit flow statements in addition to interaction with a database. Building applications with both SQL and a general-purpose language is called **database programming**

The differences in syntax and in the paradigm must be overcome

* Embedded SQL - Running SQL from within another programming language
* Procedural SQL - An extension of SQL that gives the ability to write procedures. Executed on server by DBMS
* An Application Programming Interface (API) - library of procedures or classes that gives some access

## Connections

For mysql, pip3 install mysql-connector-python

The program needs to know where to find the database, as well as how to log in

With sqlite, this just means pointing it at a specific file, or :memory:

With mySQL, this means specifying the IP address, port, username, and password

* Be sure your connection information is not included in your commit to Github

```shell
vim 1-sqliteconnection.py
vim 1-mysqlconnection.py
```

## Cursors

```python3
help(mysql.connector.cursor)
```

```shell
vim 2-sqlite_fetchall.py
vim 2-mysqlcursorFetchall.py
vim 3-cursornext.py
```



```python3
help(mysql.connector.cursor)
```

## Shared Variables

mysql defaults to port 3306 - I'm using port forwarding in virtualbox

