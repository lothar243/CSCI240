## Transactions

[YouTube - Be a Better Dev - What is a Database Transaction? (9:45)](https://www.youtube.com/watch?v=wHUOeXbZCYA&t=5s)

ACID

* Atomic - Either all or none of the operations are executed
* Consistent - Rules are not violated (Unique primary keys, business rules aren't violated, etc)
* Isolated - The transaction is processed without interference from other transactions, more on this soon
* Durable - The transaction is permanently saved to the database once committed.

## Isolation

When multiple interactions (T1 and T2) work concurrently, several scenarios are present

* Dirty read - T1 reads a value written by an uncommitted transcation T2, which is then rolled back
  The value read by T1 was invalid
* Nonrepeatable read - A transaction repeatedly reads changing data.
  T1 reads data X, T2 updates data X, T1 reads data X
  If T1 incorrectly assumes X is stable, the result of T1 is invalid
* Phantom read - One transation inserts or deletes a table row that another transaction is reading
  T1 begins reading table rows, T2 inserts a new row in to the table, T1 continues reading table rows
  The result of T1 is unpredictable

## Schedules

A transaction schedule is a sequential order of operations for multiple transactions.

Operations can be interleaved in some instances, so long as there is no conflict

Conflicts occur when one transactions reads and other writes the same data

There is no conflict if both transactions read from the data

Two schedules are said to be **equivalent schedules** if all conflicting transactions are in the same order. **Conflicting schedules** have conflicting operations in different order, and this can potentially cause differing results

A **serial schedule** is a schedule in which transactions are executed one at a time. A schedule that is equivalent to a serial schedule is said to be **serializable**

## Isolation levels

The SQL standard allows for four isolation levels

1. **SERIALIZABLE** - transactions are run in a serializable schedule with concurrent transactions. Isolation is guaranteed.
2. **REPEATABLE READ** - transactions read only committed data. After the transaction reads data, other transactions cannot update the data. REPEATABLE READ prevents most types of isolation violations but allows phantom reads. 
3. **READ COMMITTED** - transactions read only committed data. After the transaction reads data, other transactions can update the data. READ COMMITTED allows nonrepeatable and phantom reads. 
4. **READ UNCOMMITTED** - transactions read uncommitted data. READ UNCOMMITTED processes concurrent transactions efficiently but allows a broad range of isolation violations, including dirty, nonrepeatable, and phantom reads. 

## Schedules and recovery

Serializable schedules affect the concurrency system, which supports isolated transactions. Three additional schedule types affect the recovery system, which supports atomic and durable transactions:

- In a nonrecoverable schedule, one or more transactions cannot be rolled back. 
- In a cascading schedule, rollback of one transaction forces rollback of other transactions. 
- In a strict schedule, rollback of one transaction **never** forces rollback of other transactions.  

# Concurrency

## Locking

A **lock** is permission for one transaction to read and write data

A **shared lock** allows for a transaction to read, but not write, data. There can be multiple simultaneous shared locks.

An **exclusive lock** allows for the transaction to read and write data. There can be no other shared or exclusive locks when there is an exclusive lock.

**Lock scope** describes the data reserved by a lock.

A **lock manager** is the component of the system that tracks, grants, and releases locks

## Two-phase locking

* **Basic two-phase locking** - The transaction can be either in a grow or shrink phase
* **Strict two-phase locking** - holds all exclusive locks until the transaction commits or rolls back. The expand phase is the same as in basic two-phase locking, but the contract phase releases only shared locks. 
* **Rigorous two-phase locking** - holds both shared and exclusive locks until the transaction commits or rolls back. In effect, rigorous two-phase locking has no contract phase. 

## Deadlock

**Deadlock** is a state in which a group of transactions is frozen. It cannot be resolved

A **dependent transaction** is waiting for data locked by another transaction.  A **cycle** of dependent transactions indicates deadlock has occurred

Deadlock can be avoided in several ways

* **Aggressive locking** - Transactions request locks when the transaction starts
* **Data ordering** - example - rearrange locks so that locks on X occur before locks on Y
* **Timeout** - If a transaction takes too long, the transaction rolls back (or the newest transaction rolls back)
* **Cycle detection** - When a cycle is detected, the 'cheapest' transaction is rolled back

## Snapshot isolation

1. A snapshot is taken when the transaction starts
2. Updates are applied to the snapshot
3. Prior to commit, check for conflicts
4. If no conflict is detected, write the snapshot
5. If a conflict is detected, roll back

# Recovery

### Failure Scenarios

1. A **transaction failure** - Logic error, deadlock, insufficient disk space, etc
   * Results in a rollback
2. A **system failure** - Application crash or OS crash
   * Transactions that were only written to memory are likely lost
   * Roll back data written to storage by uncommitted transactions
3. A **storage media failure** - Hard drive failure
   * Redundant storage is required (RAID or backup)

### Recovery Log

A recovery log contains 4 types of records:

1. An **update record**, which indicates a transaction has changed data
2. A **compensation record**, also known as an undo record, which indicates that data has been restored after a rollback
3. A **transaction record**, which indicates a transaction boundary
4. A **checkpoint record**, which indicates that all data in main memory has been saved on storage media.

By default, mySQL only logs errors (in /var/log/mysql/error.log or /var/log/mysqld.log)

To enable logs, edit the file at /etc/mysql/mysql.conf.d/mysqld.cnf and uncomment the appropriate lines, followed by restarting the service with `sudo systemctl restart mysql.service`

# Transactions with SQL

```sql
SET [ GLOBAL | SESSION ] TRANSACTION 
ISOLATION LEVEL [ SERIALIZABLE | REPEATABLE READ | READ COMMITTED | READ UNCOMMITTED ];
```

* **SESSION** - Until the user or program disconnects
* **GLOBAL** - All transactions during this and later sessions. Can only be used by the administrator
* If neither is specified, defaults to only the next transaction in the session

A **Transaction boundary** is the first or last statement of a transaction

* START TRANSACTION
* COMMIT
* ROLLBACK

**Autocommit** can be set to on, causing individual statements to be committed immediately

```sql
SET autocommit = [ OFF | ON ];
```

COMMIT and ROLLBACK have optional keywords

* AND CHAIN - overrides the autocommit setting, starting a new transaction with settings like the prior transaction
* RELEASE ends the current session and disconnects from server

## Savepoints

A **savepoint** is a point within a transaction where partial transaction results are saved temporarily

* SAVEPOINT - saves internal transaction data and associates the data with the identifier
* RELEASE SAVEPOINT - discard savepoint
* ROLLBACK TO - resets transaction to savepoint

```sql
SAVEPOINT identifier;
ROLLBACK TO identifier;
RELEASE SAVEPOINT identifier;
```

## Checkpoints

A **dirty block** is a database block that has been updated in memory but not storage. 

A **checkpoint** suspends processing, saves everything, then resumes processing

A **fuzzy checkpoint** resumes processing while saving dirty blocks. This improves availability, but complicates recovery if the system fails

