import os

import requests


## import modules from the folder Plugins
def getModulenames():
    modules=[]
    path=os.getcwd()+'\Plugins'
    contents=os.listdir(path)
    for file in contents:
        if file[0] == '_':
            continue
        else:
            modules.append(file[:-3])
    return modules

def returndata():
    data = [[], []]
    print('getting data')
    for module in getModulenames():
        command="import Plugins." + module
        exec(command)
        command="Plugins."+module+".returnlink()"
        response=requests.get(eval(command)).text
        command="Plugins."+module+".returndata("+'"""'+response+'"""'+")"
        data0=eval(command)
        pakkumised=[x for x in data0[0] if x]
        hinnad=[x for x in data0[1] if x]
        for pakkumine in pakkumised:
            data[0].append(pakkumine)
        for hind in hinnad:
            data[1].append(hind)

    return data