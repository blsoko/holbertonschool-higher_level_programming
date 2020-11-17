-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

SELECT  tv_genres.name as 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows' FROM tv_genres INNER JOIN tv_show_genres WHERE tv_genres.id=tv_show_genres.genre_id GROUP BY tv_genres.name ORDER BY COUNT(tv_show_genres.genre_id) DESC;