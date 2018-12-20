#4.24
names=['joe','tom','barb','sue','sally']
scores=[10,23,13,18,12]
def makeDictionary(list1,list2):
    dictionary={}
    for i in range(len(list1)):
        dictionary[list1[i]]=list2[i]
    return dictionary
scoreDict=makeDictionary(names,scores)
print scoreDict
#4.25
print scoreDict['barb']
#4.26
scoreDict['john']=19
print scoreDict
#4.27
y=scoreDict.values()
y.sort()
print y
#4.28
avg=float(sum(y))/float(len(y))
print avg
#4.29
scoreDict['sally']=13
print scoreDict
#4.30
del scoreDict['tom']
print scoreDict
#4.32
def getScore(name,dictionary):
    if name in scoreDict:
        return scoreDict[name]
    else:
        return -1
print getScore('sue',scoreDict)
print getScore('jack',scoreDict)  
