from turtle import *
import colorsys

bgcolor('black')
tracer(500)

def draw():
    h = 0
    for i in range(100):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        h += 0.5
        up()
        goto(0, 0)
        down()
        fillcolor(c)  # Use the current color for filling
        begin_fill()
        rt(98)
        circle(i, 12)
        fd(200)
        fd(i)
        lt(29)
        for j in range(129):
            fd(i)
            circle(j, 299, steps=2)
        end_fill()

draw()
done()