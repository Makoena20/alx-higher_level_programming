/*
Script to list all genres from hbtn_0d_tvshows and display the number of shows linked to each.
Each record should display: <TV Show genre> - <Number of shows linked to this genre>
First column must be called genre
Second column must be called number_of_shows
Don’t display a genre that doesn’t have any shows linked
Results must be sorted in descending order by the number of shows linked
You can use only one SELECT statement
*/

SELECT genre AS genre, COUNT(show_id) AS number_of_shows
FROM tv_shows
JOIN genres ON tv_shows.id = genres.show_id
GROUP BY genre
HAVING COUNT(show_id) > 0
ORDER BY number_of_shows DESC;

