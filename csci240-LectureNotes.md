### average:
select rating, avg(rental_duration) from film group by rating;
select rating, avg(rental_duration), min(rental_duration), max(rental_duration), avg(length), min(length), max(length) from film group by rating;

### like

We can use the keyword 'like' to math with strings that are similar, with the following special characters

* % - match 0 or more characters
* _ - match 1 character

Find all countries that start with the letter 'B'

```SQL
select * from country where country like 'B%';
```

Find all countries that have B as the first letter, and a as the third

```SQL
select * from country where country like 'B_a%';
```

### sub queries

We can use the results of one select statement in another select statement

For example, if we want to find all cities in countries that begin with B

First let's just use the country_id column:

```SQL
select country_id from country where country like 'B%';
```

We will use this as the subquery as follows:

```SQL
select * from city where country_id in (select country_id from country where country like 'B%');
```

### joins

The power of relational databases likes in their relations. In order to utilize this, we want to address multiple tables at the same time, which we can do with joins

```SQL
select * from city join country on city.country_id = country.country_id limit 10;
```

this is too much, and duplicate info, so only select the columns we care about

```SQL
select city, country from city join country on city.country_id = country.country_id limit 10;
```

Another example: Find out what movies actors are in

```SQL
select * from actor join film_actor on actor.actor_id = film_actor.actor_id limit 10;
select * from actor join film_actor on actor.actor_id = film_actor.actor_id join film on film.film_id = film_actor.film_id limit 10;
select first_name, last_name, title from actor join film_actor on actor.actor_id = film_actor.actor_id join film on film.film_id = film_actor.film_id limit 10;
select first_name, last_name, title from actor join film_actor on actor.actor_id = film_actor.actor_id join film on film.film_id = film_actor.film_id order by title, last_name desc, first_name;
```

#### Inner Joins

By default we use inner joins - only actors that are present in movies, and only movies that have actors will show up in the result

#### Outer joins

[YouTube: Computer Science - Inner and Outer Joins - 7:10](https://www.youtube.com/watch?v=7yvB-tTHRfQ&list=RDCMUCSX3MR0gnKDxyXAyljWzm0Q&index=4)

What do we do with a movie that has no actors, or an actor that hasn't been in any movies?

- Left join (include all rows for the table on the left)
  If you want to find actors that don't appear in any movies

  ```SQL
  insert into actor (first_name, last_name) values ('Jeff', 'Arends');
  select first_name,film_actor.film_id from actor left join film_actor on actor.actor_id = film_actor.actor_id; -- This shows everyone
  select first_name,film_actor.film_id from actor left join film_actor on actor.actor_id = film_actor.actor_id where film_id is NULL; -- This shows only actors that aren't in movies
  ```

- Right join (include all rows for the table on the right)

  This would give all movies regardless of whether they had an actor

  ```SQL
  insert into film (title, language_id) values ('test movie', 1)
  select actor_id, title from film_actor right join film on film_actor.film_id = film.film_id where actor_id is null;
  ```

* Full outer join (include all rows for both tables)
  
* Cross (cartesian product)
  each item in the first with each item in the second

  ```SQL
  select * from store cross join staff_list;
  ```

### Aliasing

This isn't exclusive to joins, but it's usually where it's seen. It allows us to change the name used to refer to a table

```sql
select a.first_name,a.actor_id from actor as a join film_actor as fa on a.actor_id = fa.actor_id;
```

We can even alias the attribute names

```sql
select first_name as actorName from actor limit 10;
```

This allows us to join a table with itself

```sql
create table employees ( id tinyint unsigned, name varchar(20), managerID tinyint unsigned , primary key (id), foreign key (managerID) references employees(id) );

insert into employees values (1, 'Board of directors', null), (2, 'CEO', 1), (3, 'CSO', 1), (4, 'VP of Security', 3), (5, 'Security Manager', 4);

select * from employees join employees as bosses on employees.managerID = bosses.id;
```

This also allows other subqueries. To find the shortest average runtime based on rating

```sql
select avg(length), rating from film group by rating;

select min(len) from (select avg(length) as len, rating from film group by rating) as averages;
```

### Views

Frequently used queries can be stored to be used again

```SQL
create view average_runtime as select avg(length) as len, rating from film group by rating;

select * from average_runtime where len = (select min(len) from average_runtime);
```

Though, possibly a better way of accomplishing this (in this instance) would be to sort in ascending order and just take the first
```sql
select * from average_runtime order by len limit 1;
```
 These stored views have the appearance of being an additional table

```sql
create view actor_movie as select first_name, last_name, title from actor join film_actor on actor.actor_id = film_actor.actor_id join film on film.film_id = film_actor.film_id;

show tables;

drop view actor_movie;
```



