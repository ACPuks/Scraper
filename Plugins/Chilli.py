from bs4 import BeautifulSoup
def returndata(response):
    pakkumised = []
    hinduus = []
    soup=BeautifulSoup(response)
    pakutav = soup.findAll('div', {'class': 'product-desc'})
    for pakkumine in pakutav:
        temp = pakkumine.find('h2')
        if temp:
            pakkumised.append(temp.text)

            
    # leiab kõik hinnad lehelt
    for hind in soup.find_all("p", "special-price"):
        # kontrollib, et hind poleks tühi
        if str(hind.contents[0]) != '':
            # kontrollib, et hind ei algaks a-ga
            if str(hind.contents[0]).strip()[0] == 'a':
                # lisab hinna ilma alguse osata ja ilma lõpus oleva euro märgita
                hinduus.append(str(hind.contents[0]).strip()[4:-1])
            else:
                hinduus.append(str(hind.contents[0]).strip()[:-1])
    return [pakkumised, hinduus]

# tagastab lehekülje lingi
def returnlink():
    return 'http://chilli.ee'
