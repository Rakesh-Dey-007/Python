import math
from turtle import *

def heart_y(k):
    return 12*math.cos(k) - 5*math.cos(2*k) - 2*math.cos(3*k) - math.cos(4*k)

def heart_x(k):
    return 15*math.sin(k)**3

speed(0)
bgcolor("black")

for i in range(10000):
    x = heart_x(i)*20
    y = heart_y(i)*20

    goto(x,y)
    color("red")
    goto(0,0)

done()