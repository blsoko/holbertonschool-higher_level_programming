-- script that lists the number of records
SELECT score, COUNT(score) as `number` FROM second_table GROUP BY score DESC;
