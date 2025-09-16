#lab4 Ousman Touray
#calls function
import turtle
from lab4Function import *
turtle.title("Ninja")
ninja = turtle.Turtle()
drawSquare(ninja, 180)
#turtle location
print("position is: ", ninja.pos())
#direction of turtle
print("heading in: ", turtle.heading())
ninja.penup()
ninja.setpos(-300, 300)
ninja.pendown()
ninja.pencolor("blue")
drawSquare(ninja, 75)

#draw a dot at 300,300
ninja.penup()
ninja.setpos(300, 300)
ninja.pencolor("red")
ninja.dot()
ninja.pendown()
ninja.pensize(5)
ninja.pencolor("green")
ninja.penup()
ninja.setpos(200,200)
ninja.dot()

#write text
ninja.penup()
ninja.setpos(-300,-300)
ninja.pencolor("brown")
ninja.pendown()
ninja.pensize(2)
ninja.write("This is cool", font=("Arial", 20, "bold"))

#draw circle
ninja.penup()
ninja.setpos(300, -300)
ninja.pencolor("yellow")
ninja.fillcolor("yellow")
ninja.pendown()
ninja.begin_fill()
ninja.circle(90)
ninja.end_fill()
ninja.penup()

# home
ninja.home()
ninja.pendown()
ninja.pencolor("brown")
ninja.fillcolor("brown")
ninja.begin_fill()
ninja.circle(90)
ninja.end_fill()
##TODO here you will add the code for drawing a triangle, octagon.
turtle.done()
