import turtle
myTurtle=turtle.Turtle()
def drawRectangle(myTurtle,height,width):
    for i in range(2):
        myTurtle.forward(width)
        myTurtle.right(90)
        myTurtle.forward(height)
        myTurtle.right(90)
drawRectangle(myTurtle,100,50)