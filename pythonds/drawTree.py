from turtle import *


def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t)
        t.left(40)
        tree(branchLen-10, t)
        t.right(20)
        t.backward(branchLen)

        
myTurtle = Turtle()
myWin = myTurtle.getscreen()

myTurtle.left(90)
myTurtle.up()
myTurtle.backward(300)
myTurtle.down()
myTurtle.color('green')

tree(110, myTurtle)

myWin.exitonclick()