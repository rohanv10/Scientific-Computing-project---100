import turtle
myTurtle=turtle.Turtle()
def drawSpiral(myTurtle,maxSide):
    myTurtle.up()
    myTurtle.forward(200)
    myTurtle.down()
    for sideLength in range(1,maxSide+1,5):
        myTurtle.forward(sideLength)
        myTurtle.right(90)
drawSpiral(myTurtle,100)

myTurtle2=turtle.Turtle()
def drawSpiral(myTurtle2,maxSide):
    for sideLength in range(1,maxSide+1,5):
        myTurtle2.forward(sideLength)
        myTurtle2.left(90)
drawSpiral(myTurtle2,100)