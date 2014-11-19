import os
import requests
import Modules
## import modules from the folder Modules
def getModulenames():
    modules=[]
    path=os.path.realpath(__file__)+'\Modules'
    contents=os.listdir(path)
    for file in contents:
        if file == '__init__.py':
            continue
        else:
            modules.append(file[:-3])
    return modules
def getlink(modulename)
    return eval('Modules.'+modulename+'.returnlink()')
def getresponse(address):
    #get the html file of the address and return it
    return requests.get(address)
def getsoup(modulename,file):
    # get the soup for that particular site
    return eval('Modules.'+modulename+'.returnsoup(file)')
#get the data of that particular soup of
def getdata(modulename,soup):
    return eval('Modules.'+modulename+'.returndata(soup)')
