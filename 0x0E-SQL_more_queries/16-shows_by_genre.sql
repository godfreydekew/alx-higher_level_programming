--  lists all shows, and all 
-- genres linked to that show,
SELECT t.`title`, g.`name`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS s
       ON g.`id` = s.`genre_id`

       RIGHT JOIN `tv_shows` AS t
       ON t.`id` = s.`show_id`
 ORDER BY t.`title`, g.`name`;
