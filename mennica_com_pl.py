import requests as rq
from bs4 import BeautifulSoup as bs

URL = "https://www.mennica.com.pl/monety-i-numizmaty/katalog?type=srebrna%20moneta"

page = rq.get(URL);
soup = bs(page.content, "html.parser")
all = soup.find(id ="component_wrapper_1625584")
units = all.find_all("div", class_="repository_product item")

results = []

for unit in units:
        nameDiv = unit.find("div", class_="repository_product item")
        print(nameDiv)
        #name = unit.find("a", class_="product__name")
        #priceDiv = unit.find("div", class_="product__prices")
        #price = priceDiv.find("strong", class_="price")
        #
        #results.append({
        #    'name': name.contents[0],
        #    'price': price.contents[0]
        #})

