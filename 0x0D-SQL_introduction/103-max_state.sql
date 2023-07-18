-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)

SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;