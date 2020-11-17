-- script that lists the number of records
SELECT score, COUNT(score) FROM second_table GROUP BY score DESC;
