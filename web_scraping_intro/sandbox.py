import urllib.request
import bs4 as bs


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

for movie_href in movie_hrefs:
    print(movie_href)

# print(movie_hrefs, end="\n")
print(len(movie_hrefs))