from bs4 import BeautifulSoup
def returndata(response):
    pakkumised = []
    hinduus = []
    soup=BeautifulSoup(response)
    for section in soup.findAll('div', {'class': 'product-container'}):
        try:
            pakkumine=section.find('h2').text
            hind=section.find('p', {'class': 'special-price'}).text.strip()
            pakkumised.append(pakkumine)
            hinduus.append(hind)
        except:
            pass

    return [pakkumised, hinduus]

# tagastab lehekülje lingi
def returnlink():
    return 'http://chilli.ee'
