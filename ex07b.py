import turtle
from random import randint

def randAngle():
    return randint(15, 45)

def randRange():
    return randint(5, 25)

def centerTurtle(t):
    t.left(90)
    t.up()
    t.backward(100)

def tree(branchLen,t):
    if branchLen >= 75:
        t.pencolor("Brown")
    elif branchLen >= 50:
        t.pencolor("Dark Green")
    elif branchLen >= 25:
        t.pencolor("Green")
    else:
        t.pencolor("Light Green")
    if branchLen > 5:
        angle = randAngle()
        range = randRange()
        t.pensize(branchLen/10)
        t.forward(branchLen)
        t.right(angle)
        tree(branchLen-range,t)
        t.left(angle * 2)
        tree(branchLen-range,t)
        t.right(angle)
        t.penup()
        t.backward(branchLen)
        t.pendown()

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    centerTurtle(t)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()