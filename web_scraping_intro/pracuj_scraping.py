import bs4 as bs
from urllib.request import Request, urlopen

req = Request('http://pracuj.pl/praca', headers={'User-Agent': 'Mozilla/5.0'})
pracuj_html = urlopen(req).read()

pracuj_soup = bs.BeautifulSoup(pracuj_html, 'lxml')

# print(pracuj_soup.prettify())

job_adverts = pracuj_soup.findAll('a', {'class': 'offer-details__title-link'})

job_titles = []

for job_advert in job_adverts:
    job_title = job_advert.get_text()
    job_titles.append(job_title)

for job_title in job_titles:
    print(job_title)

# print(h3)