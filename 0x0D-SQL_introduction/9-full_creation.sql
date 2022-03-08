-- create a table "second_table" in database hbtn
-- and add  multiples rows
CREATE TABLE if NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
INSERT INTO second_table(`id`, `name`, `score`) VALUES (1, "JHON", 10), (2, "ALEX", 3);
