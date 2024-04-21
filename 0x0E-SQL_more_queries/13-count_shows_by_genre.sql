/*
Script to list all genres from hbtn_0d_tvshows
and display the number of shows linked to each genre
*/

SELECT genre AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
GROUP BY genre
ORDER BY number_of_shows DESC;

