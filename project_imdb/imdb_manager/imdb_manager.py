import pymysql
from project_imdb.config import host, user, database, password # wciągamy plik z hasłem, loginem, etc.
from project_imdb.imdb_manager.imdb_queries import add_actor_query, get_actor_id_query


class Actor:
    """
    Holds data about actors
    """

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

    def addActor(self, actor):
        """
        adds actor t actor table given actor object
        :param actor: actor object
        :return:
        """
        cursor = self.conn.cursor()
        cursor.execute(add_actor_query %  (actor.first_name, actor.last_name, actor.nationality))
        self.conn.commit()

    def getActorId(self, actor):
        cursor = self.conn.cursor()
        cursor.execute(get_actor_id_query % (actor.first_name, actor.last_name))
        return cursor.fetchall()[0][0]



if __name__ == "__main__":
    imdb_manager = ImdbManager(host, user, database, password)
    actor = Actor(first_name="Jerzy", last_name="Stuhr", nationality="POL")
    print(imdb_manager.getActorId(actor))


