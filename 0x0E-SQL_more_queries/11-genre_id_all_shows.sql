-- lists all shows contained in hbtn_0d_tvshows
-- If a show doesn’t have a genre, display NULL
SELECT tv.title, tg.genre_id
        FROM tv_shows AS tv
                LEFT JOIN tv_show_genres AS tg
                ON tv.id = tg.show_id
        ORDER BY tv.title, tg.genre_id;
