add_actor_query = "insert actors (firstname, lastname, nationality) values ('%s', '%s', '%s')"

get_actor_id_query = """
select id_a from actors where firstname = '%s' and lastname = '%s' order by id_a limit 1;
"""