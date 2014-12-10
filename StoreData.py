import csv
### Stores data as CSV
def store(time,content):
    with open('data.csv','w', newline='', encoding='UTF-8') as csvfile:
        writer=csv.writer(csvfile)
        for pakkumine in range(len(content[0])):
            if content[0][pakkumine]=='':
                print('Tühi pakkumine')
                pass
            else:
                try:
                    writer.writerow([content[0][pakkumine],content[1][pakkumine],content[2][pakkumine] ,time])
                except:
                    pass
    csvfile.close()