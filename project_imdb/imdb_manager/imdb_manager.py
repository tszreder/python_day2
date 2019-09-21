import pymysql
from project_imdb.config import host, user, database, password # wciągamy plik z hasłem, loginem, etc.
from project_imdb.imdb_manager.imdb_queries import add_actor_query, get_actor_id_query, add_person_query


class Person:

    def __init__(self, first_name, last_name, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality


class ImdbManager:


    def __init__(self, host, user, database, password):

        self.conn = pymysql.connect(host = host, user = user, password = password, database=database, charset = "utf8")

        # self.c = self.conn.cursor()
        # print("Ustanowiono połączenie z bazą danych")
        # sql_query = "show tables"
        # self.c.execute(sql_query)
        # rows = self.c.fetchall()
        # for row in rows:
        #     print(row)

    def addPerson(self, person, table):
        cursor = self.conn.cursor()
        cursor.execute(add_person_query % (table, person.first_name, person.last_name, person.nationality))
        self.conn.commit()


    def addActor(self, person):
        self.addPerson(person, "actors")


    def addDirector(self, person):
        self.addPerson(person, "directors")


    def getActorId(self, actor):
        cursor = self.conn.cursor()
        cursor.execute(get_actor_id_query % (actor.first_name, actor.last_name))
        return cursor.fetchall()[0][0]



if __name__ == "__main__":
    imdb_manager = ImdbManager(host, user, database, password)
    actor = Person(first_name="John", last_name="Travolta", nationality="USA")
    imdb_manager.addActor(actor)

    # print(imdb_manager.getActorId(actor))


