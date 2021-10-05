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

The program needs to know where to find the database, as well as how to log in

```shell
vim 1-connection.py
```

## Cursors

```shell
vim 2-cursorFetchall.py
vim 3-cursornext.py
```

```python3
help(mysql.connector.cursor)
```

On zyBooks, the C syntax is different... FETCH instead of fetchone

## Shared Variables

pip3 install mysql-connector-python

mysql defaults to port 3306 - I'm using port forwarding in virtualbox
