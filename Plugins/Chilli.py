from bs4 import BeautifulSoup


def returndata(response):
    pakkumised = []
    hinduus = []
    page = []
    soup=BeautifulSoup(response)
    allowedchars="0123456789,. "
    for section in soup.findAll('div', {'class': 'product-container'}):
        try:
            firstnum=''
            lastnum=False
            pakkumine=section.find('h2').text
            hind=section.find('p', {'class': 'special-price'}).text.strip()
            if pakkumine[-1] == '%':
                pakkumine=pakkumine[0:-4]
            for x in hind:
                try:
                    if str(x) in allowedchars and firstnum =='':
                        firstnum=hind.index(x)+1
                    elif firstnum == True and str(x) not in allowedchars and lastnum == False:
                        lastnum=hind.index(x)
                except:
                    pass

            try:
                hind=hind[firstnum-1:lastnum]
            except:
                pass
            pakkumised.append(pakkumine)
            hinduus.append(hind)
            page.append('Chilli')
        except Exception:
            continue

    return [pakkumised, hinduus, page]

# tagastab lehekülje lingi
def returnlink():
    return 'http://chilli.ee'
