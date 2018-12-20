#2.29
def func(result):
    answer=0
    if result==100:
        answer=1
    else:
        answer=2
    return answer
func(100)
#2.30
def gp(score):
    if score>90:
        gradeP=4
        if 89>score>80:
            gradeP=3
        if 79>score>70:
            gradeP=2
        else:
            69>score>60
        gradeP=1
    else:
        gradeP=0
    return gradeP
#2.31
def GP(score):
    if score>90:
        gradeP=4
    elif 89>score>80:
        gradeP=3
    elif 79>score>70:
        gradeP=2
    elif 69>score>60:
        gradeP=1
    else:
        gradeP=0
    return gradeP
#2.32
def leapYear(year):
    if year % 4 == 0 and year % 400 != 0:
        return True
    else:
        return False
#2.33
def finalC(pounds):
    if pounds>100:
         cost=pounds*0.32 + 6
    else:
        cost=pounds*0.32 + 7.5
    return cost
finalC(210)
#2.34
def largest(num1,num2,num3):
    if num1>num2 and num1>3:
        return num1 
    elif num2>num1 and num2>num3:
        return num2 
    else:
        return num3
largest(1,2,3)
#2.1
import math
circumference=0
def circleC(radius):
    circumference=2*math.pi*radius
    return circumference
circleC(3)
#2.2
import math
area=0
def circleA(radius):
    area=math.pi*radius*radius
    return area
circleA(3)
#2.6
def isEven(number):
    if number%2==0:
        return true
    else:
        return false