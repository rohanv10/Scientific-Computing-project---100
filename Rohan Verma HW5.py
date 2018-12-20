#3.1
name='Rohan Verma'

#3.2
name='Rohan Verma'
print (name[0:4])

#3.3
name='Rohan Verma'
print (name[6:10])

#3.4
name='Rohan Verma'
print name[6:10]+','+name[0:4]

#3.5
name='Rohan Verma'
print len(name[0:4])

#3.6
S='s'
P='p'
miss= 'm'+'i'+S*2+'i'+S*2+'i'+P*2+'i'
print miss

#3.7
name= 'Roy G Biv'
for i in range (len(name)+1):
    print(name[0:i])

#3.8
S='s'
P='p'
miss= 'm'+'i'+S+S+'i'+S+S+'i'+P+P+'i'
print miss.count(S)

#3.9
S='s'
P='p'
miss= 'm'+'i'+S+S+'i'+S+S+'i'+P+P+'i'
print miss.replace('iss','ox')

#3.10
S='s'
P='p'
miss= 'm'+'i'+S+S+'i'+S+S+'i'+P+P+'i'
print miss.index('p')

#3.11
py='python'
print py.centre(20)

#3.12
#The ord() function returns the Unicode value of the given character
#So the difference is that capital 'A' and lowercase 'a' are represented by different integer values.

#3.13
def CS(R):
    return ord(R)
print CS('5')

#3.14
def letterToIndex(character):
    return ord(character)-97
print letterToIndex('b')

#3.15
def letterToIndex(character):
    return ord(character)+97
print letterToIndex('c')

#3.16
def grade(score):
    if score>=90:
        grade='A'
    elif 89>= score >= 80:
        grade='B'
    elif 79>= score >= 70:
        grade='C'
    elif 69>= score >= 60:
         grade='D'
    else:
        grade='F'
    return grade