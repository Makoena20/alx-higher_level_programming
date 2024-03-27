/*
 * Task: Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
 */

-- SELECT statement to calculate average temperature by city and order by temperature descending
SELECT city, ROUND(AVG(temperature), 4) AS avg_temp
FROM cities
GROUP BY city
ORDER BY avg_temp DESC;

