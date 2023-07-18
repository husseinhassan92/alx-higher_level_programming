-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)

SELECT city, MAX(value) as max_temp
FROM temperatures
GROUP BY city
ORDER BY max_temp DESC;