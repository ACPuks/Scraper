__author__ = 'Allan'
from bs4 import BeautifulSoup
def returndata(response):
    pakkumised = []
    hinduus = []
    soup=BeautifulSoup(response)
    for section in soup.findAll('li', {'class': 'z_offer'}):
        try:
            pakkumine=section.find('h2').text
            hind=section.find('div', {'class': 'price-new'}).text.strip()
            pakkumised.append(pakkumine)
            hinduus.append(hind)
        except:
            pass


    return [pakkumised, hinduus]
def returnlink():
    return 'http://zave.ee'