-- list all cities contained in the database "hbtn"
SELECT cities.id, cities.name, state.name FROM cities
RIGHT JOIN states ON states.id = cities.states_id
ORDER BY city.id
