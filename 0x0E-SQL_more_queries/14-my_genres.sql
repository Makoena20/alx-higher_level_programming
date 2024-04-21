/*
  Script to list all genres of the show Dexter from the hbtn_0d_tvshows database.
  The tv_shows table contains only one record where title = Dexter (but the id can be different).
  Each record should display: tv_genres.name
  Results must be sorted in ascending order by the genre name.
  You can use only one SELECT statement.
*/

SELECT UPPER(tv_genres.name) AS name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;

