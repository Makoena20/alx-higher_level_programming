/*
Script to list all Comedy shows in the database hbtn_0d_tvshows
*/

-- Select all Comedy shows from the tv_shows table
SELECT tv_shows.title
FROM tv_shows
JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;

