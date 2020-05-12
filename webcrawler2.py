from bs4 import BeautifulSoup
import requests

def trade_spider(max_pages):
    page = 1
    # while page < max_pages:
    url = 'https://www.javatpoint.com/python-tutorial'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.find('div', {'class': 'leftmenu'}).findAll('a'):
        href = "https://www.javatpoint.com/"+ link.get('href');
        title = link.string
        print(title)
        print(href)
    page +=1

trade_spider(1)

