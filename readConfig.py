
settingsDict={}
with open('config.txt','r') as f:
    for line in f.readlines():
        key,value=line.split('=')
        key=key.replace('\n','')
        value=value.replace('\n','')
        settingsDict[key] = value


def returnValue(key):
    return settingsDict[key]

