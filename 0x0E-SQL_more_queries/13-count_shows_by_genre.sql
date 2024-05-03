/* Script to list all genres and the number of shows linked to each */
SELECT genre, COUNT(*) AS number_of_shows
FROM shows
GROUP BY genre
HAVING COUNT(*) > 0
ORDER BY COUNT(*) DESC;

