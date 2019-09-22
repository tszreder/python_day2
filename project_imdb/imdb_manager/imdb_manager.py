import pymysql
from project_imdb.config import host, user, database, password # wciągamy plik z hasłem, loginem, etc.
from project_imdb.imdb_manager.imdb_queries import get_person_id_query, add_person_query, add_genre_query, get_genre_id_query


class Person:

    def __init__(self, first_name, last_name, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality


class Genre:

    def __init__(self, name):
        self.name = name


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

    def _addPerson(self, person, table):
        cursor = self.conn.cursor()
        cursor.execute(add_person_query % (table, person.first_name, person.last_name, person.nationality))
        self.conn.commit()
        return self._getPersonId(person, table)

    def addActor(self, person):
        self._addPerson(person, "actors")

    def addDirector(self, person):
        self._addPerson(person, "directors")

    def _getPersonId(self, person, table):
        cursor = self.conn.cursor()
        cursor.execute(get_person_id_query % (table, person.first_name, person.last_name))
        return cursor.fetchall()[0][0]

    def addGenre(self, genre):
        cursor = self.conn.cursor()
        cursor.execute(add_genre_query % genre.name)
        self.conn.commit()
        return self._getGenreId(genre)

    def _getGenreId(self, genre):
        cursor = self.conn.cursor()
        cursor.execute(get_genre_id_query % genre.name)
        return cursor.fetchall()[0][0]

if __name__ == "__main__":
    imdb_manager = ImdbManager(host, user, database, password)
    # genre = Genre('Action')
    # print(imdb_manager.addGenre(genre))

    actor = Person(first_name="Steven", last_name="Spielberg", nationality="USA")
    # imdb_manager.addDirector(actor)
    print(imdb_manager._getPersonId(actor, "directors"))




