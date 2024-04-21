-- List all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement

SELECT TV_GENRES.name AS name, SUM(RATING) AS rating
FROM TV_SHOWS
JOIN TV_SHOWS_GENRES ON TV_SHOWS.id = TV_SHOWS_GENRES.tv_show_id
JOIN TV_GENRES ON TV_GENRES.id = TV_SHOWS_GENRES.tv_genre_id
GROUP BY TV_GENRES.name
ORDER BY rating DESC;

