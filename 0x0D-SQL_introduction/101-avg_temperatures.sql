-- displays the average temperature 
-- ordered by temperature (descending)
-- GROUPED BY CITY
SELECT `city` , AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
