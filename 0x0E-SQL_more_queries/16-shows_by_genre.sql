/*
Script to list all shows and their linked genres from the hbtn_0d_tvshows database
If a show doesn’t have a genre, display NULL in the genre column
Results sorted in ascending order by show title and genre name
*/

SELECT tv_shows.title, IFNULL(tv_genres.name, 'NULL') AS name
FROM tv_shows
LEFT JOIN tv_genres ON tv_shows.id = tv_genres.show_id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
