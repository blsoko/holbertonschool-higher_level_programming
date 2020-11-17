-- script that computes the score average of all records in the table
SELECT CAST(AVG(score) AS DECIMAL(7,4)) AS `average` FROM second_table;
