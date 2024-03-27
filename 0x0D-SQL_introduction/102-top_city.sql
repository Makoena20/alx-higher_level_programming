/*
   Script to display the top 3 cities with the highest average temperature during July and August.
*/

-- SELECTING THE TOP 3 CITIES WITH THE HIGHEST AVERAGE TEMPERATURE DURING JULY AND AUGUST
SELECT city, AVG(temperature) AS avg_temp
FROM cities
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

