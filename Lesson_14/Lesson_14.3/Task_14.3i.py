import turtle as t
import math as m
import random as r


def figure(n, square):
    size = (square * 4 * m.tan(m.radians(180 / n)) / n) ** 0.5
    color = tuple((r.randint(0, 255) for _ in range(3)))
    t.fillcolor(color)
    t.begin_fill()

    t.forward(size / 2)
    t.left(360 / n)
    for i in range(n - 1):
        t.forward(size)
        t.left(360 / n)
    t.forward(size / 2)
    t.end_fill()


def main():
    t.speed(0)
    t.hideturtle()
    for y in range(130, -200, -75):
        for x in range(-150, 170, 75):
            t.penup()
            t.goto(x, y)
            t.pendown()
            figure(r.randint(3, 6), 1800)


main()