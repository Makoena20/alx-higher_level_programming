-- This script lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
-- Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Only one SELECT statement is used

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

