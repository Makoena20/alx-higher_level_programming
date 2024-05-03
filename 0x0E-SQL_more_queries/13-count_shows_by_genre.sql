/*
Script to list all genres from hbtn_0d_tvshows and display the number of shows linked to each.
*/

SELECT genre, COUNT(*) AS number_of_shows
FROM shows
GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;

