# Physical Design

## Storage Media

Hard drives - 250 bytes per sector (or 4kB for newer ones). SSDs use pages, whose sizes can vary.

Databases and file systems use a uniform size, called a block, when transferring data between memory and storage.

Transactional applications typically access data by row, and to minimize block transfers the data can be arranged so that rows are stored together - this is called **row oriented storage**

Analytical applications may be more interested in just reading a few columns from many rows, and the data can be arrange to be **column-oriented** for more optimal storage/retrieval.

## Table Structure

* Heap - No order is imposed. Fast writes, slow reads
* Sorted table - Table is sorted by a column. Slow writes, fast reads
* Hash table - Data is grouped together based on a hash function. Fast for individual reads/writes, slow for bulk reads/writes
* Table cluster - Rows from multiple tables are interleaved based on a cluster key. Fast for joining with that cluster key, slow for joining on other values. Slow to update cluster key also. Not commonly used

## Indexes

[YouTube - Socratica - Introduction to Indexes (9:56)](https://www.youtube.com/watch?v=fsG1XaZEa78)

Indexes are used to help find data when you want to read. 

* Typically a single column that is sorted and contains a pointer to the location of the full row (stored elsewhere)
* Easier to keep the index table sorted, and not have to rewrite all the data whenever something new is inserted. 
* Able to have a heap for the majority of your data, and still be able to find it quickly (assuming you're using the indexed column)
* Potentially able to be stored entirely in memory

Sorted index allows the posibility of a **binary search**

* Look at the halfway point, is the target before or after? Repeatedly cut search space in half

You can have multiple indexes, but there are costs

* More space
* Maintaining sort
* Time to build originally

Sparse vs dense indexing - A dense index contains an entry for every row. A sparse index requires you to accommodate for the fact that not all rows have pointers somehow

## Multi-level indexes

The index has multiple levels, starting sparse and possibly ending dense

Allows for the possibility of indexing very large databases

Different schemes exist for multi-level indexes

## Physical Design

### Engines

InnoDB - Transactional DB (Default)

MyISAM - Analytical applications with limited data updates

MEMORY - all data is stored in memory

### CREATE/DROP/SHOW INDEX

CREATE INDEX IndexName on TableName (Column1, Column2, etc);

DROP INDEX IndexName on TableName

SHOW INDEX FROM TableName;

### EXPLAIN Statement

EXPLAIN can show how a select, insert, update, or delete statement will be executed

Useful for the following

* Deciding indexes (creating new or dropping unused indexes)

* Identifying slow queries (finding which query is slow, and determine why)

  