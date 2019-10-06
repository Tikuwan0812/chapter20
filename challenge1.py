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
        with open('headline_articles_url.txt', 'w', encoding='utf-8') as f:
            for tag in sp.find_all('a', class_='DY5T1d'):
                url = tag.get('href')
                f.write('\n' + url)

news = 'https://news.google.com/'
Scraper(news).scrape()