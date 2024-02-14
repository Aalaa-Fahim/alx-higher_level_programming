-- listing all records of the table of the database
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
