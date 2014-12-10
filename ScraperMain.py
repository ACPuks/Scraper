import datetime
import csv
from time import sleep
from os import stat

import GetData
import StoreData


def checkData():
    print('checking data')
    try:
        #proovi faili avada
        print('trying to open file')
        csv_in=open('data.csv','r',encoding='UTF-8')
        print('successful opening of file')
    except:
        print('failed to open file')
        #kui faili ei ole/ei saa avada, tekita uus fail
        StoreData.store(datetime.datetime.now(), GetData.returndata())
        print('reopening file')
        csv_in=open('data.csv','r',encoding='UTF-8')
    lugeja=csv.reader(csv_in)
    print('created reader')
    if stat('data.csv').st_size == 0:
        print('fail on tühi, genereerib uued andmed')
        StoreData.store(datetime.datetime.now(), GetData.returndata())
        print('reopening file cause was empty')
        csv_in=open('data.csv','r',encoding='UTF-8')
    else:
        pass
    pakkumised=[]
    hinnad=[]
    pages=[]
    for rida in lugeja:
        pakkumine, hind, page, aeg = rida
        #kontrollib kas pakkumised on aegunud ehk üle 15min vanad
        if datetime.datetime.strptime(aeg,'%Y-%m-%d %H:%M:%S.%f') < datetime.datetime.now()-datetime.timedelta(minutes=15):
            print('Data is old')
            csv_in.close()
            #toob uued andmed sisse
            StoreData.store(datetime.datetime.now(), GetData.returndata())
            break
        else:
            #väljastab andmed
            pakkumised.append(pakkumine)
            hinnad.append(hind)
            pages.append(page)
    csv_in.close()
    print('Successfully retrieved data')
    return [pakkumised, hinnad, pages]

#programmi pealoop
while True:
    #saab andmed
    andmed=checkData()
    #magab 20min
    sleep(20*60)