
get_person_id_query = """
select id from %s where firstname = '%s' and lastname = '%s' order by id limit 1;
"""

add_person_query = """
INSERT INTO %s (firstname, lastname, nationality) VALUES ('%s', '%s', '%s');
"""

add_genre_query = """
INSERT INTO genres (genreName) VALUES ('%s');
"""

get_genre_id_query = """
select id_g from genres where genreName = '%s';
"""

add_film_row_query = """
insert into films (Title, RelYear, OrigTitle, DurationMins, Ranking, Voters, Rating)
 values ('%s', '%s', '%s', '%s', '%s', '%s', '%s')
"""

add_actor_in_film_row = """
insert into actor_in_film (id_f, id_a) values (%s, %s)
"""

add_film_has_genre_row = """
insert into film_has_genre (id_f, id_g) values (%s, %s)
"""