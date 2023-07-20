-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- each record should display: tv_genres.name - number_shows
-- don’t display a genre that doesn’t have any shows linked
-- results must be sorted in descending order by the number of shows linked
-- can use only one SELECT statement
-- the database name will be passed as an argument of the mysql command

SELECT tv_shows.title
      FROM tv_shows
     WHERE tv_shows.title NOT IN (
    SELECT tv_shows.title
      FROM tv_shows
INNER JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
     WHERE tv_genres.name = "Comedy")
  ORDER BY tv_shows.title;