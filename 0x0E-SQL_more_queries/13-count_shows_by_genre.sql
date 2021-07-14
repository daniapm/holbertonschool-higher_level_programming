-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name AS genres COUNT(*) AS number_of_shows
    FROM tv_genres
    JOIN tv_show_genres
    ON tv_show_genres.genres_id = tv_genres.id
ORDER BY number_of_shows
GROUP BY tv_show_genres.genres_id
DESC;
