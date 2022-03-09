-- create a database hbtn_0d_usa and the table state
-- id INIT unique, aute generated. can´t be null and is a primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256),
	PRIMERY KEY (id)
);
