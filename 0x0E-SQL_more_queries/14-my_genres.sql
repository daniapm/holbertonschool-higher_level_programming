-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_shows.title
    FROM tv_genres
    WHERE tv_shows.title = Dexter
    AND tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows
DESC;
