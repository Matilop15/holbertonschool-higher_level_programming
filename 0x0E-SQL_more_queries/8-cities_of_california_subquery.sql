-- list all cities of california in the database "hbtn"
SELECT id, name FROM cities;
WHERE state_id = (
	SELECT id FROM cities WHERE name = "California";
);
