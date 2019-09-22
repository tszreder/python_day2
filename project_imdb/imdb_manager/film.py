def zero_if_none(val):
    if val is None:
        return 0
    else:
        return val


def empty_list_if_none(val):
    if val is None:
        return []
    else:
        return val


# class Person:
#
#     def __init__(self, first_name, last_name, nationality):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.nationality = nationality
#
#
# class Genre:
#
#     def __init__(self, name):
#         self.name = name


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
        self.duration = zero_if_none(duration)
        self.director = director
        self.actors = empty_list_if_none(actors)
        self.voters = zero_if_none(voters)
        self.rating = zero_if_none(rating)
        self.ranking = zero_if_none(ranking)
        self.orig_title = orig_title
        self.genres = empty_list_if_none(genres)

if __name__ == "__main__":
    film = Film(title="Skazani na Shawshank", rel_year=1994)
    print(film)


