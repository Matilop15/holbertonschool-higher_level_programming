-- list all cities contained in the database "hbtn"
SELECT cities.id, cities.name, states.name 
FROM cities JOIN states ON states.id = cities.states_id
ORDER BY cities.id ASC;
