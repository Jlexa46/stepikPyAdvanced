import turtle
import math


def heart():
    turtle.fillcolor('red')
    turtle.begin_fill()
    for t in range(630):
        t *= 0.01
        x = 128 * math.sin(t) ** 3
        y = 8 * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t) - 5)
        turtle.goto(x, y)
    turtle.end_fill()


heart()