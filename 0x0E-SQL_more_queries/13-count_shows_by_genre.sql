-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT COUNT(*) AS tv_shows.genre, tv_show_genres.number_of_shows
    FROM tv_shows
    JOIN tv_show_genres
    ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id
DESC;
