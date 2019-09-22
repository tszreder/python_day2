import pymysql
from project_imdb.config import host, user, database, password # wciągamy plik z hasłem, loginem, etc.
from project_imdb.imdb_manager.imdb_queries \
    import get_person_id_query, add_person_query, add_genre_query, \
    get_genre_id_query, add_film_row_query, add_actor_in_film_row, add_film_has_genre_row
from project_imdb.imdb_manager.film import Film

class Person:

    def __init__(self, first_name, last_name, nationality=None):
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
        return self._addPerson(person, "actors")

    def addDirector(self, person):
        return self._addPerson(person, "directors")

    def _getPersonId(self, person, table):
        cursor = self.conn.cursor()
        cursor.execute(get_person_id_query % (table, person.first_name, person.last_name))
        try:
            return cursor.fetchall()[0][0]
        except IndexError:
            return None

    def addGenre(self, genre):
        cursor = self.conn.cursor()
        cursor.execute(add_genre_query % genre.name)
        self.conn.commit()
        return self._getGenreId(genre)

    def _getGenreId(self, genre):
        cursor = self.conn.cursor()
        cursor.execute(get_genre_id_query % genre.name)
        try:
            return cursor.fetchall()[0][0]
        except IndexError:
            return None

    def addFilm(self, film):
        """
        adds film to database including transition table values
        :param film:
        :return:
        """

        actor_ids = []
        for actor in film.actors:
            actor_id = self._getPersonId(actor, 'actors')
            if actor_id is None:
                actor_id = self.addActor(actor)
            actor_ids.append(actor_id)

        genre_ids = []
        for genre in film.genres:
            genre_id = self._getGenreId(genre)
            if genre_id is None:
                genre_id = self.addGenre(genre)
            genre_ids.append(genre_id)

        if film.director is not None:
            director_id = self._getPersonId(film.director, 'directors')
            if director_id is None:
                director_id = self.addDirector(film.director)

        film_id = self._addFilmRow(film, director_id)

        for actor_id in actor_ids:
            self._addActorInFilmRow(film_id, actor_id)

        for genre_id in genre_ids:
            self._addFilmHasGenre(film_id, genre_id)

    def _addFilmRow(self, film, director_id):
        cursor = self.conn.cursor()
        cursor.execute(add_film_row_query % (film.title, film.rel_year, film.orig_title,
                                             film.duration, film.ranking, film.voters, film.rating, director_id))
        self.conn.commit()
        return cursor.lastrowid

    def _addActorInFilmRow(self, film_id, actor_id):
        cursor = self.conn.cursor()
        cursor.execute(add_actor_in_film_row % (film_id, actor_id))
        self.conn.commit()

    def _addFilmHasGenre(self, film_id, genre_id):
        cursor = self.conn.cursor()
        cursor.execute(add_film_has_genre_row % (film_id, genre_id))
        self.conn.commit()


if __name__ == "__main__":
    imdb_manager = ImdbManager(host, user, database, password)
    # genre = Genre('Action')
    # print(imdb_manager.addGenre(genre))

    # actor = Person(first_name="Jerzy", last_name="Hoffmann", nationality="POL")
    # imdb_manager.addDirector(actor)
    # print(imdb_manager._getPersonId(actor, "directors"))
    # et_film = Film(title='Skazani na Shawshank', rel_year='1994', orig_title='Shawshank Redemption',
    #                ranking='1', rating='9.2')
    # print(imdb_manager._addFilmRow(et_film))
    # imdb_manager._addActorInFilmRow(2, 3)

    # print(imdb_manager._getPersonId(actor, 'actors'))

    # actors = [Person("Sylvester", "Stallone"), Person("Arnold", "Schwarzenegger")]
    director = Person("Steven", "Spielberg")
    imdb_manager.addDirector(director)
    print(imdb_manager._getPersonId(director,'directors'))
    # genres = [Genre("SciFi"), Genre("Family")]
    #
    # film = Film(title="ET", rel_year=1983, actors=actors, genres=genres, director=director)
    # imdb_manager.addFilm(film)



