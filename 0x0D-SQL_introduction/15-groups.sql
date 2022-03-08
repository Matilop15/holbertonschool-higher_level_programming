-- list the number of records with same score in the table second_table
SELECT score, COUNT(`score`) as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
