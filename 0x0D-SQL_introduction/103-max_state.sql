/*
Script to display the max temperature of each state (ordered by State name)
*/

/* Selecting the maximum temperature for each state */
SELECT State, MAX(Temperature) AS max_temp
FROM states
GROUP BY State
ORDER BY State;

