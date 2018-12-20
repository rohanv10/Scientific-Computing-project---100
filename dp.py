import turtle
roh=turtle.Turtle()
def drawPolygon(roh,length,numSides): 
    angle = 360 / numSides
    for i in range(numSides):
        roh.forward(length)
        roh.right(angle)
drawPolygon(roh,150,5)