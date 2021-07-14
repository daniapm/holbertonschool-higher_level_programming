-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_shows.name
    FROM tv_genres
    JOIN tv_show_genres
    ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_show_genres.genre_id
ORDER BY tv_genres.name
ASC;
