-- Script to list all genres from hbtn_0d_tvshows and display the number of shows linked to each
SELECT genre AS genre, COUNT(*) AS number_of_shows
FROM shows
WHERE genre IS NOT NULL
GROUP BY genre
ORDER BY number_of_shows DESC;

