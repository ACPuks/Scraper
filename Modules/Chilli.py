def returndata(soup):
    pakkumised=[]
    hinduus=[]
    #otsib kõik pakkumised üles lehel
    for pakkumine in soup.select('div.product-desc a[href^=/vaata-pakkumist]'):
        #kontrollib kas pakkumine ei ole vaata ja kas pakkumine ei ole tühi
        if pakkumine.contents[0] != 'Vaata ' and str(pakkumine.contents[0]) != '':
            #kontrollib kas pakkumise lõpus on % märk ja kui on eemaldab selle ja %
            if pakkumine.contents[0][-1]=='%':
                pakkumised.append(pakkumine.contents[:-4])
            else:
                pakkumised.append(pakkumine.contents[0])
            
    #leiab kõik hinnad lehelt
    for hind in soup.find_all("p","special-price"):
        #kontrollib, et hind poleks tühi
        if str(hind.contents[0]) != '':
            #kontrollib, et hind ei algaks a-ga
            if str(hind.contents[0]).strip()[0] == 'a':
                #lisab hinna ilma alguse osata ja ilma lõpus oleva euro märgita
                hinduus.append(str(hind.contents[0]).strip()[4:-1])
            else:
                hinduus.append(str(hind.contents[0]).strip()[:-1])
    return [pakkumised,hinduus]
#tagastab soup-i
def returnsoup(file):
    #tagastab soupi veidike teistmoodi kuna  :)
    with open(file, 'rb') as html:
        return BeautifulSoup(html)
#tagastab lehekülje lingi
def returnlink():
    return 'http://chilli.ee'
