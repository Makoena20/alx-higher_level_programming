/*
Script to list all shows contained in the database hbtn_0d_tvshows,
displaying each show's title and genre_id.
Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.
If a show doesn’t have a genre, NULL is displayed.
*/

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

