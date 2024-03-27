-- Script to list the number of records with the same score in the second_table of the hbtn_0c_0 database

-- Count the number of records for each score and display the results sorted by the number of records (descending)
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
