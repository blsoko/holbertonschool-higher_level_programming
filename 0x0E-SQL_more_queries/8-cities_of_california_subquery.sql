-- script that lists all the cities of California

SELECT states.id, cities.name FROM states, cities WHERE states.id=cities.state_id;
