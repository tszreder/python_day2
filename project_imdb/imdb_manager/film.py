class Film:
    """
    holds information about films
    """

    def __init__(self,
                 title,
                 rel_year=None,
                 duration=None,
                 director=None,
                 rating=None,
                 voters=None,
                 ranking=None,
                 orig_title=None,
                 actors=None,
                 genres=None):
        """

        :param title:
        :param rel_year:
        :param duration:
        :param director:
        :param rating:
        :param voters:
        :param ranking:
        :param orig_title:
        :param actors: list of actors as a list of strings
        :param genres: list of genres as a list of strings
        """

        self.title = title
        if type(rel_year) == "int":
            self.rel_year = rel_year
        else:
            self.rel_year = int(rel_year)
        self.duration = duration
        self.director = director
        self.rating = rating
        self.actors = actors
        self.voters = voters
        self.ranking = ranking
        self.orig_title = orig_title
        self.genres = genres

if __name__ == "__main__":
    film = Film(title="Skazani na Shawshank", rel_year=1994)
    print(film)