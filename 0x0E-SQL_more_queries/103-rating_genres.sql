/*
Script to list all genres in the hbtn_0d_tvshows_rate database by their rating
Each record displays: tv_genres.name - rating sum
Results are sorted in descending order by rating
*/

SELECT tv_genres.name, SUM(rating) AS rating
FROM tv_genres
JOIN tv_shows ON tv_genres.id = tv_shows.genre_id
JOIN ratings ON tv_shows.id = ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;

