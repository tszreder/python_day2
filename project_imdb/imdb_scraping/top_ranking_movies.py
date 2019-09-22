from project_imdb.imdb_manager.imdb_manager import ImdbManager, Person, Genre
from project_imdb.config import host, user, database, password
from project_imdb.imdb_manager.film import Film
import bs4 as bs
import urllib.request


imdb_manager = ImdbManager(host, user, database, password)

imdb_base_url = "https://imdb.com"

# w film_rank_content zawarta jest cała strona jako string
film_rank_content = urllib.request.urlopen(imdb_base_url + "/chart/top?ref_=nv_mv_250").read()

#twórzę obiekt beautiful soup
film_rank_soup = bs.BeautifulSoup(film_rank_content, "lxml")

# daj mi treści wszystkich znaczniki treści td, które maja klasę titleColumn, zwraca listę wszystkich tych znczaników jako listę,
# każdy element listy jest nadal obiektem beautiful soup i można nadal korzystać z tych samych metod
movie_tds = film_rank_soup.findAll('td', {'class': 'titleColumn'})

movie_hrefs = []
for movie_td in movie_tds:
    movie_href = movie_td.find('a').attrs['href'] # szukam wszystkich elementów a i zwracam ich atrybut href
    movie_hrefs.append(imdb_base_url + movie_href)

# print(type(movie_tds[0]))
#
# print(movie_tds[0])

# wchodzimy na stronę dotyczącą konkretnego filmu


counter = 0
for movie_href in movie_hrefs:
    counter += 1
    film_detail_content = urllib.request.urlopen(movie_href).read()
    film_detail_soup = bs.BeautifulSoup(film_detail_content, "lxml")

    # title i year
    title_wrapper_div = film_detail_soup.find('div',{'class': 'title_wrapper'})
    year = title_wrapper_div.find('h1').find('span').find('a').text.strip()
    title = title_wrapper_div.find('h1').text
    title = title.replace('(%s)' % year, '').strip()

    # director & actors
    credit_summary_items = film_detail_soup.findAll('div', {'class': 'credit_summary_item'})
    for credit_summary_item in credit_summary_items:
        #director
        if 'Director' in credit_summary_item.find('h4').text:
            director = credit_summary_item.find('a').text
            director_split = director.split(' ')
            d_first_name = director_split[0]
            d_last_name = director_split[-1]
            director = Person(d_first_name, d_last_name)

        #actors
        actors = []
        if 'Stars' in credit_summary_item.find('h4').text:
            for a in credit_summary_item.findAll('a'):
                if not 'full cast' in a.text:
                    a_split = a.text.split(' ')
                    a_first_name = a_split[0]
                    a_last_name = a_split[-1]
                    actor = Person(a_first_name, a_last_name)
                    actors.append(actor)

    #genres
    see_more_elems = film_detail_soup.findAll('div', {'class': 'see-more inline canwrap'})
    for see_more_elem in see_more_elems:
        if 'genres' in see_more_elem.find('h4').text.lower():
            genres = []
            for a in see_more_elem.findAll('a'):
                genre = Genre(a.text.strip())
                genres.append(genre)

    film = Film(title=title, orig_title=title, rel_year=year, director=director, actors=actors, genres=genres)
    imdb_manager.addFilm(film)
    print(title)
    if counter > 10:
        break


    # print(year)
    # print(director)
    # print(actors)
    # print(genres)
    # print("title: '%s'; genres: '%s'" % (title, ', '.join([el.name for el in genres])))
    # break

