/*
  Task: Write a script that lists all shows and their associated genres from the database hbtn_0d_tvshows.
  If a show doesn’t have a genre, display NULL in the genre column.
  Each record should display: tv_shows.title - tv_genres.name
  Results must be sorted in ascending order by the show title and genre name.
*/

-- List all shows and their associated genres
SELECT tv_shows.title, IFNULL(tv_genres.name, 'NULL') AS name
FROM tv_shows
LEFT JOIN show_genres ON tv_shows.id = show_genres.show_id
LEFT JOIN tv_genres ON show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;

