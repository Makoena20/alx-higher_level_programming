-- This script lists all shows from hbtn_0d_tvshows_rate by their rating
-- Each record displays: tv_shows.title - rating sum
-- Results are sorted in descending order by the rating
-- Only one SELECT statement is used

SELECT tv_shows.title, SUM(rating) AS rating
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.tv_show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;

