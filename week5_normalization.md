# Normalization

[YouTube - Computer Science - Introduction to Normalization](https://www.youtube.com/watch?v=y03oYWDLu0Q)

Normalization is the process of minimizing redundancy from a relation or set of relations

Redundant data is problematic for multiple reasons

* It takes up more space
* It can fall out of sync

Our solution is to normalize the data, but removing redundancy has its drawbacks

* More complex database
  * More tables
  * More complicated queries
* Slower queries

We have to weigh the pros and cons when choosing how much to normalize

## First Normal Form

Every attribute in the relation is a single-valued attribute (aka atomic)

Each row must be unique

No repeating attributes (Course Title 1, Course Title 2, Course Title 3)

[YouTube - Computer Science Database Normalisation - 7:26](https://www.youtube.com/watch?v=jgUeOjImOOw)

Normalization Lecture PDF, page 13 

Example that's not in first normal form:

```sql
select * from nicer_but_slower_film_list where id=1;
```

Another example: <https://en.wikipedia.org/wiki/First_normal_form>

## Second Normal Form

Must be in first normal form

Must not contain any partial dependency

[Youtube - Computer Science - Second Normal Form - 9:20](https://www.youtube.com/watch?v=9L10Q1nAfyg) - Talk about functional dependency more from an "adding a new item" standpoint

Examples from PDF

Additional examples on wikipedia: <https://en.wikipedia.org/wiki/Second_normal_form>

## Third Normal Form

Must be in 2NF

A relation has no transitive functional dependencies on the primary key

[YouTube - Computer Science - Third Normal Form - 8:29](https://www.youtube.com/watch?v=_K7fcFQowy8&t=328s)

Examples from PDF

More examples on wikipedia: <https://en.wikipedia.org/wiki/Third_normal_form>

## Boyce-Codd Normal Form (BCNF)

If a relational schema is in BCNF then all redundancy based on functional dependency has been removed, although other types of redundancy may still exist. 

A relational schema R is in Boyce–Codd normal form if and only if for every one of its dependencies X → Y, at least one of the following conditions hold:

* X → Y is a trivial functional dependency (Y  is a subset of X)
* X is a superkey for schema R - In other words X contains a candidate key

| Court | Start time | End time | Rate type |
| ----- | ---------- | -------- | --------- |
| 1     | 09:30      | 10:30    | SAVER     |
| 1     | 11:00      | 12:00    | SAVER     |
| 1     | 14:00      | 15:30    | STANDARD  |
| 2     | 10:00      | 11:30    | PREMIUM-B |
| 2     | 11:30      | 13:30    | PREMIUM-B |
| 2     | 15:00      | 16:30    | PREMIUM-A |

- Each row in the table represents a court booking at a tennis  club. That club has one hard court (Court 1) and one grass court (Court  2)
- A booking is defined by its Court and the period for which the Court is reserved
- Additionally, each booking has a Rate Type associated with it. There are four distinct rate types:
  - SAVER, for Court 1 bookings made by members
  - STANDARD, for Court 1 bookings made by non-members
  - PREMIUM-A, for Court 2 bookings made by members
  - PREMIUM-B, for Court 2 bookings made by non-members

The table is in 3NF, but it fails to be in BCNF because Rate type → Court, but Rate type is not a candidate key

The design can be amended so that it meets BCNF:

| Rate type | Court | Member flag |
| --------- | ----- | ----------- |
| SAVER     | 1     | Yes         |
| STANDARD  | 1     | No          |
| PREMIUM-A | 2     | Yes         |
| PREMIUM-B | 2     | No          |

| Member flag | Court | Start time | End time |
| ----------- | ----- | ---------- | -------- |
| Yes         | 1     | 09:30      | 10:30    |
| Yes         | 1     | 11:00      | 12:00    |
| No          | 1     | 14:00      | 15:30    |
| No          | 2     | 10:00      | 11:30    |
| No          | 2     | 11:30      | 13:30    |
| Yes         | 2     | 15:00      | 16:30    |

## Achievability of BCNF

In some cases, a non-BCNF table cannot be decomposed into tables that  satisfy BCNF and preserve the dependencies that held in the original  table. Beeri and Bernstein showed in 1979 that, for example, a set of  functional dependencies {AB → C, C → B} cannot be represented by a BCNF  schema.[[4\]](https://en.wikipedia.org/wiki/Boyce–Codd_normal_form#cite_note-Beeri-4)

Consider the following non-BCNF table whose functional dependencies follow the {AB → C, C → B} pattern:

| Person   | Shop type   | Nearest shop   |
| -------- | ----------- | -------------- |
| Davidson | Optician    | Eagle Eye      |
| Davidson | Hairdresser | Snippets       |
| Wright   | Bookshop    | Merlin Books   |
| Fuller   | Bakery      | Doughy's       |
| Fuller   | Hairdresser | Sweeney Todd's |
| Fuller   | Optician    | Eagle Eye      |

For each Person / Shop type combination, the table tells us which shop of this type is geographically nearest to the person's home. We assume for simplicity that a single shop cannot be of more than one type.

The candidate keys of the table are:

- {Person, Shop type},
- {Person, Nearest shop}.

Because all three attributes are prime attributes (i.e. belong to  candidate keys), the table is in 3NF. The table is not in BCNF, however, as the Shop type attribute is functionally dependent on a non-superkey: Nearest shop.

# Normalization is not...

As a database administrator, your job is not to clean up the data that users put in. If a user chooses to put nearly the same value in multiple fields this is their choice. 

It is not a good practice to make changes to a database without reason. If a database already has a surrogate key, there is no reason to create another one.

The goal is not to remove rows that are similar data either.

It is not beneficial to split a table just to create two tables

