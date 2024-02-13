-- displays the average temperature 
-- ordered by temperature (descending)
-- GROUPED BY CITY
-- displays the top 3 of cities 
SELECT `city` , AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` IN (7, 8)
GROUP BY `city`
ORDER BY `avg_temp` DESC; 
LIMIT 3;
