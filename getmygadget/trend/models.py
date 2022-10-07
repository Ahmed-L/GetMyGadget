from abc import ABC,abstractmethod
from bs4 import BeautifulSoup
import requests
import re

class ScrapTrend(ABC):
    @abstractmethod
    def fetch(self):
        pass

class Web1(ScrapTrend):
    url = "https://ajkerdeal.com/en/category/gadgets"

    def fetch(self):
        name = []
        price = []
        link = []
        img = []
        response = requests.get(self.url)

        data = response.text
        soup = BeautifulSoup(data, 'html.parser')

        products = soup.find_all('div', {'class': 'deal-info-container'})
        for p in products:
            name.append(p.find('span', {'class': 'deal-title-container'}).text)
            temp = p.find('span', {'class': 'deal-price-container'}).text
            temp = re.sub('\W+', '', temp)
            price.append(temp)
            link.append(p.find('a').get('href'))
            img.append(p.find('img', {'class': 'deal_image'}).get('src'))

        return name,price,link,img

class Web2(ScrapTrend):
    url = "https://www.startech.com.bd/gadget?sort=rating&order=DESC"

    def fetch(self):
        name = []
        price = []
        link = []
        img = []
        response = requests.get(self.url)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')

        products = soup.find_all('div', {'class': 'product-thumb'})

        for p in products:
            name.append(p.find('h4', {'class': 'product-name'}).text)
            temp = p.find('div', {'class': 'price space-between'}).text
            temp = re.sub('\W+', '', temp)
            price.append(temp)
            link.append(p.find('a').get('href'))
            img.append(p.find('img').get('src'))

        return name, price, link, img