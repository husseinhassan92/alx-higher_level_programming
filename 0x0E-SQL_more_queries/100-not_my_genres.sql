-- script that uses the hbtn_0d_tvshows database to lists all genres not linked to Dexter
-- tv_shows table contains only one record where title = Dexter (but the id can be different)
-- each record should display: tv_genres.name
-- results must be sorted in ascending order by the genre name
-- can use max two SELECT statements
-- the database name will be passed as an argument of the mysql command

SELECT tv_genres.name
      FROM tv_genres
     WHERE tv_genres.name NOT IN (
        SELECT tv_genres.name
        FROM tv_genres
        INNER JOIN tv_show_genres
            ON tv_show_genres.genre_id = tv_genres.id
        INNER JOIN tv_shows
            ON tv_show_genres.show_id = tv_shows.id
        WHERE tv_shows.title = "Dexter")
    ORDER BY tv_genres.name;