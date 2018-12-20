#4.1
myList=[7,9,'a','cat',False]
print myList

#4.2
#a
myList.append(3.14)
myList.append(7)
print myList
#b
myList.insert(2,'dog')
print myList
#c
myList.index("cat")
print myList
#d
myList.count(7)
print myList
#e
myList.remove(7)
print myList
#f
myList.pop(myList.index('dog'))
print myList

#4.3
a="the quick brown fox"
b=a.split( )
print b

#4.4
c="mississippi"
d=c.split('i')
print d 

#4.5
def Split(sentence):
    e=sentence.split( )
    return len(e)
print Split('my name is Rohan')

#4.6
#a
def count(aList,item):
    var=list.count(item)
    return var
#b
def in(aList,item):
    if item>=0:
        return True
    else:
        return False
#c
def reverse(aList):
    aList.reverse()
    return aList
#e
def insert(aList,item,index):
    aList.insert(index,item)
    return aList