import turtle
alon=turtle.Turtle()
def drawRectangle(alon,sideLength):
    for i in range(2):
        alon.forward(sideLength)
        alon.right(90)
        alon.forward(2*sideLength)
        alon.right(90)
drawRectangle(alon,100)