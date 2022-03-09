-- list all cities contained in the database "hbtn"
SELECT cities.id, cities.name, states.name 
FROM cities JOIN states ON cities.states_id = states.id
ORDER BY cities.id ASC;
