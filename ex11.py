import turtle

win = turtle.Screen()

myTurtle = turtle.Turtle()
myTurtle.speed(50)
myTurtle.penup()
myTurtle.setposition((-win.canvwidth / 2, -win.canvheight / 2))
myTurtle.pendown()
myTurtle.left(60)

def drawKoch(t, len, currentIteration, iteration):
  if currentIteration == iteration:
    t.forward(len)
  else:
    currentLen = len / 3.0
    drawKoch(t, currentLen, currentIteration + 1, iteration)
    t.left(60)
    drawKoch(t, currentLen, currentIteration + 1, iteration)
    t.right(120)
    drawKoch(t, currentLen, currentIteration + 1, iteration)
    t.left(60)
    drawKoch(t, currentLen, currentIteration + 1, iteration)

for i in range(3):
  drawKoch(myTurtle, 500, 0, 2)
  myTurtle.right(120)
