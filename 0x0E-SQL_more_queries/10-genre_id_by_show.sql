-- each record should display: tv_shows.title - tv_show_genres.genre_id
-- results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- can use only one SELECT statement
-- the database name will be passed as an argument of the mysql command

SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows
    INNER JOIN tv_show_genres
        ON tv_show_genres.show_id = tv_shows.id
    ORDER BY tv_shows.title, tv_show_genres.genre_id;