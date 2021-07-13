-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.id, cities.name FROM states, cities
WHERE states.name = 'California' AND cities.states.id = state_id
ORDER BY cities.id DESC;