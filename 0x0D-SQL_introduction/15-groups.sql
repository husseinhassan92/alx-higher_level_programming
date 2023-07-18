-- lists the `score` and number of occurances with each score with 'number'
-- displays this data sorted by number in descending order

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;