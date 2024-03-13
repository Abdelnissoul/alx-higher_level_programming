-- Lists all records of the table with a name value in my MySQL
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
