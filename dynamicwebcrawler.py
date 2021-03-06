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
        # print(title)
        # print(href)
        get_single_item_data(href)
    page +=1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('div',{'class':'margin-left'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = "https://www.javatpoint.com/" + link.get('href');
    print(href)
trade_spider(3)

