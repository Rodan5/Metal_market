import requests as rq
from bs4 import BeautifulSoup as bs

def MetalMarket():
    URL = "https://www.metalmarket.eu/pl/menu/srebrne-monety-851.html?filter_traits%5B1%5D=&filter_traits%5B512%5D=&filter_traits%5B510%5D=481&filter_pricerange=&filter_traits%5B304%5D=&filter_traits%5B69%5D="
    page = rq.get(URL);
    soup = bs(page.content, "html.parser")
    all = soup.find(id="search")
    units = all.find_all("div", class_="product col-6 col-sm-4 col-xl-3 pt-3 pb-md-3")
    
    results = []
    for unit in units:
        nameDiv = unit.find("a", class_="product__icon d-flex justify-content-center align-items-center")
        name = unit.find("a", class_="product__name")
        priceDiv = unit.find("div", class_="product__prices")
        price = priceDiv.find("strong", class_="price")
        
        results.append({
            'name': name.contents[0],
            'price': price.contents[0]
        })
    return results