-- list all cities of california in the database "hbtn"
SELECT id, name FROM hbtn_0d_usa;
WHERE state_id (
	SELECT id FROM cities WHERE name = "California";
);
