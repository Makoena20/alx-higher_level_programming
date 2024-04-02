/* 
   Script to list all genres from hbtn_0d_tvshows and display the number of shows linked to each genre
   Each record should display: <TV Show genre> - <Number of shows linked to this genre>
   First column must be called genre
   Second column must be called number_of_shows
   Don’t display a genre that doesn’t have any shows linked
   Results must be sorted in descending order by the number of shows linked
*/

SELECT genre AS genre, COUNT(*) AS number_of_shows
FROM shows
WHERE genre IS NOT NULL
GROUP BY genre
ORDER BY COUNT(*) DESC;
