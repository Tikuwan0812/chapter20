import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        result = urllib.request.urlopen(self.site)
        html = result.read()
        sp = BeautifulSoup(html, 'html.parser')
        for tag in sp.find_all('h3', class_='ipQwMb ekueJc RD0gLb'):
            url = tag.a.get('href')
            if url is None:
                continue
            print(url)

news = 'https://news.google.com/'
Scraper(news).scrape()