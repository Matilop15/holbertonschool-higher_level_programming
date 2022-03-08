-- import temperatures and display top 3 of citis temperature
-- during July and August order by temperature descending
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = '7' OR month = '8'
GROUP BY city ORDER BY avg_temp DESC
LIMIT 3;
