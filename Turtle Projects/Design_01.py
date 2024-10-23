import turtle
import pyfiglet

heading = pyfiglet.figlet_format('Turtle Design')
print(heading)

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("green")

t.speed(0)
t.penup()
t.goto(0,-150)
t.pendown()

a = 0
b = 0
while True:
    t.forward(a)
    t.left(b)
    a += 3
    b += 1
    if b == 210:
        break
    t.hideturtle()


turtle.done()