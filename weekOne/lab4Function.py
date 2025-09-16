#Lab 4 Ousman Touray
# use of the turtle
def drawSquare(myTurtle, sideLength):
    no_sides = 4
    angle = 360/no_sides
    for i in range(no_sides):
        myTurtle.forward(sideLength)
        myTurtle.right(angle)