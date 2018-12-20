#Authors:Alan Medina & Rohan Verma 
#Purpose:Final Project
#Course:CSCI100
#Date:December 12th 2018

import turtle
from turtle import *
screen=turtle.Screen()
screen.setup(580,580)
image="snl.gif"
screen.addshape(image)
bg=turtle.Turtle()
bg.shape(image)

title("Turtle Keys")
player1=Turtle()
player1.up()
player1.goto(-252,-266)
player1.color('red')

def a1():
    player1.forward(56)
def a2():
    player1.left(90)
def a3():
    player1.right(90)
def a4():
    player1.back(56)

onkey(a1, "Up")
onkey(a2, "Left")
onkey(a3, "Right")
onkey(a4, "Down")

player2=Turtle()
player2.up()
player2.color('blue')
player2.goto(-252,-252)

def b1():
    player2.forward(56)
def b2():
    player2.left(90)
def b3():
    player2.right(90)
def b4():
    player2.back(56)

onkey(b1, "w")
onkey(b2, "a")
onkey(b3, "d")
onkey(b4, "s")

listen()
mainloop()

