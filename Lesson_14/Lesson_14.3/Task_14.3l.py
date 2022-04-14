from turtle import *
from math import radians, sin, cos

Screen().setup(800, 300)
speed(8)

solars = (('Солнце', 'yellow', 50, (-100, 40)),
          ('Меркурий', 'DarkOrange', 10, (-55, 37)),
          ('Венера', 'DarkOrange', 13, (-10, 39)),
          ('Земля', 'green', 12, (25, 42)),
          ('Марс', 'indianred', 8, (80, 25)),
          ('Юпитер', 'DarkOrange', 24, (150, 25)),
          ('Сатурн', 'DarkOrange', 24, (210, 33)),
          ('Уран', 'CadetBlue', 16, (255, 33)),
          ('Нептун', 'blue', 16, (300, 45)),
          ('Плутон', 'DarkOrange', 5, (150, 20)))


def write_name(name):
    penup()
    right(90)
    forward(25)
    fillcolor('black')
    write(name, align='center')
    backward(10)
    left(90)


def ellipse(a, b):
    dx = xcor()
    dy = ycor()
    for deg in range(361):
        rad = radians(deg)
        x = a * sin(rad) + dx
        y = -b * cos(rad) + b + dy
        goto(x, y)


penup()
goto(-200, 0)
pendown()

for s in solars:
    write_name(s[0])
    fillcolor(s[1])
    begin_fill()
    pendown()
    circle(s[2])
    end_fill()
    penup()
    goto(s[3])

pendown()
fillcolor('black')
ellipse(30, 15)