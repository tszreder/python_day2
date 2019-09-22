
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