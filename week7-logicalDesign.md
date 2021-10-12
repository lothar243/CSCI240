# Logical Design
## Implementing entities

Primary keys should be stable, simple, and meaningless

Independent entities become independent tables

* Choose a primary key
  * Preferably a single-column key, but a composite key may work, else an artificial key

Subtype entities become subtype tables

* The primary key is identical to the supertype primary key
* The primary key is also a foreign key

Dependent entities become dependent tables

* A foreign key references the master table(s) primary key(s)
* Another key that makes the composite primary key unique, possibly an artificial key
* If the dependency is one-to-one, the second column is unnecessary and the foreign key is enough

## Implementing relationships

Many-to-one relationships, foreign key goes on 'many' side

One-to-one relationships, foreign key can go on either side, but usually the table with fewer rows

Many-to-many relationships use a third table

* The new table contains two foreign keys
* The primary key of the new table is the composite of the two foreign keys
* Table name is the two related tables, with optional qualifier

## Implementing attributes

Singular attributes remain in the initial table

Plural attributes move to a new table

* Plural attribute and foreign key of initial table, this becomes the composite key
* The name is the initial table name, plus the attribute name

## Normalization/Denormalization

Verify functional dependencies. Recall that for BCNF, the only functional dependencies should be on a full candidate key.

# Todo

Normalize speakers.csv and stolen guns for them

Talk about the music database ER diagram, relate the track to the invoice of the 'Heather Designs'

Step through process of the Heather Designs ER diagram to create SQL tables