-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- each record should display: tv_genres.name - number_shows
-- don’t display a genre that doesn’t have any shows linked
-- results must be sorted in descending order by the number of shows linked
-- can use only one SELECT statement
-- the database name will be passed as an argument of the mysql command

SELECT tv_shows.title, tv_genres.name
    FROM tv_shows
    LEFT JOIN tv_show_genres
        ON tv_show_genres.show_id = tv_shows.id
    LEFT JOIN tv_genres
        ON tv_show_genres.genre_id = tv_genres.id
    ORDER BY tv_shows.title, tv_genres.name;