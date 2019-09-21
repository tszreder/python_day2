get_actor_id_query = """
select id_a from actors where firstname = '%s' and lastname = '%s' order by id_a limit 1;
"""

add_person_query = """
INSERT INTO %s (firstname, lastname, nationality) VALUES ('%s', '%s', '%s');
"""