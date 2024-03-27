/*
This script lists all records of the table second_table of the database hbtn_0c_0 in MySQL server.
It filters out rows without a name value and displays the score and name, ordered by descending score.
*/

-- SELECT records with name and order by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

