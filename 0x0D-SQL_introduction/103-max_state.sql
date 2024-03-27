-- Task: Write a script that displays the max temperature of each state (ordered by State name).

-- Display the max temperature of each state
SELECT state, MAX(temp) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
