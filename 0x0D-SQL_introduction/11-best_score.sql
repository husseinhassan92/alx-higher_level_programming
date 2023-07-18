-- display score and name fields of data in table
-- ordered from greatest to least and greater than 10

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;