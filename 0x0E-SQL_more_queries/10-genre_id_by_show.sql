-- lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.
SELECT tv.title, tg.genre_id
	FROM tv_shows AS tv 
		INNER JOIN tv_show_genres AS tg
		ON tv.id = tg.show_id
	ORDER BY tv.title, tg.genre_id;
