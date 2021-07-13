-- script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name  states.name FROM states
JOIN cities ON cities.state_id = state.id
ORDER BY cities.id DESC;
