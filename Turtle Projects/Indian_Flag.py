import turtle
from turtle import *
import pyfiglet

highlight = pyfiglet.figlet_format('Indian Flag')
print(highlight)

#screen for output
screen = turtle.Screen()
screen.title("Drawing Indian Flag")
screen.setup(600, 400)

# Defining a turtle Instance
t = turtle.Turtle()
speed(0)

# initially penup()
t.penup()
t.goto(-200, 125)
t.pendown()

# Orange Rectangle 
t.color("orange")
t.begin_fill()
t.forward(400)
t.right(90)
t.forward(83)
t.right(90)
t.forward(400)
t.end_fill()
t.left(90)
t.forward(83)

# Green Rectangle
t.color("green")
t.begin_fill()
t.forward(83)
t.left(90)
t.forward(400)
t.left(90)
t.forward(83)
t.end_fill()

# Big Blue Circle
t.penup()
t.goto(35, 0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(35)
t.end_fill()

# Big White Circle
t.penup()
t.goto(30, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(30)
t.end_fill()

# Mini Blue Circles
t.penup()
t.goto(-28, -4)
t.pendown()
t.color("navy")
for i in range(24):
    t.begin_fill()
    t.circle(1.5)
    t.end_fill()
    t.penup()
    t.forward(7.5)
    t.right(15)
    t.pendown()
    
# Small Blue Circle
t.penup()
t.goto(10, 0)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
# Spokes
t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(1)
for i in range(24):
    t.forward(30) 
    t.backward(30) 
    t.left(15)
    

#output window
turtle.done()