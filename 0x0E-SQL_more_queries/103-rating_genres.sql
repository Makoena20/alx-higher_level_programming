/*
Script to list all genres by their rating
Only one SELECT statement allowed
Results sorted in descending order by rating
*/

SELECT tv_genres.name, SUM(tv_genres.rating) AS rating
FROM tv_genres
JOIN tv_shows ON tv_genres.show_id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY rating DESC;

