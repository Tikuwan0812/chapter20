import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
    
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = 'html.parser'
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all('a', class_='DY5T1d'):
            url = tag.get('href')
            print('\n' + url)

news = 'https://news.google.com/'
Scraper(news).scrape()