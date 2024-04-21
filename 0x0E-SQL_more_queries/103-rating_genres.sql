-- 103-rating_genres.sql
-- Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement

SELECT
    tv_genres.name,
    SUM(tv_shows.rating) AS rating
FROM
    tv_genres
JOIN
    tv_shows ON tv_genres.id = tv_shows.genre_id
GROUP BY
    tv_genres.name
ORDER BY
    rating DESC;
