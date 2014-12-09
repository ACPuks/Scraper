import datetime
import csv
import time
import os

import GetData
import StoreData


pakkumised=[]
hinnad=[]

def checkData():
    print('checking data')
    pakkumised=[]
    hinnad=[]
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
    if os.stat('data.csv').st_size == 0:
        print('fail on tühi, genereerib uued andmed')
        StoreData.store(datetime.datetime.now(), GetData.returndata())
        print('reopening file cause was empty')
        csv_in=open('data.csv','r',encoding='UTF-8')
    else:
        pass
    for rida in lugeja:
        pakkumine, hind, aeg = rida
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
    csv_in.close()
    print('Successfully retrieved data')
    return [pakkumised, hinnad]

#programmi pealoop
while True:
    #saab andmed
    andmed=checkData()
    print(andmed)
    #generate html table from data here...
    #magab 20min
    time.sleep(20*60)