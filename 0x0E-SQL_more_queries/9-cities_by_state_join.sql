/*
  Task:
  Write a script that lists all cities contained in the database hbtn_0d_usa.

  Each record should display: cities.id - cities.name - states.name
  Results must be sorted in ascending order by cities.id
  You can use only one SELECT statement

  Requirements:
  - All SQL keywords should be in uppercase
  - All your SQL queries should have a comment just before
  - All your files should start by a comment describing the task
*/

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

