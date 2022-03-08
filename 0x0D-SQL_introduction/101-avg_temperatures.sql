-- import temperatures and display the average temperature
-- by city order by temperature descending

SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city ORDER BY avg_temp DESC;
