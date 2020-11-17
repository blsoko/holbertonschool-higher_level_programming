-- script that lists all the cities of California

SELECT states.id, cities.name FROM states, cities WHERE states.name=(SELECT states.name FROM states WHERE name="California") and states.id=cities.state_id; 

