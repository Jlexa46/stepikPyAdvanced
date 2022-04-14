import turtle
import random


def star(r):
    color = '#F7F795'
    turtle.pencolor(color)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(random.randint(0, r))
    turtle.end_fill()
    turtle.penup()


def starsky(r, canvx, canvy):
    for i in range(150):
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(random.randint(-(canvx // 2), canvx // 2), random.randint(-(canvy // 2), canvy // 2))
        star(r)


def rect(sidex, sidey, color):
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()
    for i in range(2):
        turtle.forward(sidex)
        turtle.right(90)
        turtle.forward(sidey)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()


def bilding(canvx, canvy):
    color = 'blue'
    turtle.penup()
    turtle.goto(-(canvx // 2), -canvy * 0.2)
    rect(canvx, canvy // 3, color)
    turtle.goto(-(canvx // 2.8), 0)
    rect(canvx * 0.2, canvy * 0.2, color)
    turtle.goto(-(canvx // 5.5), canvy // 2.9)
    rect(canvx * 0.22, canvy * 0.55, color)
    turtle.goto(0, -canvy * 0.1)
    rect(canvx * 0.22, canvy * 0.11, color)
    turtle.goto(canvx * 0.2, canvy * 0.1)
    rect(canvx * 0.18, canvy * 0.4, color)
    turtle.goto(canvx * 0.28, -canvy * 0.02)
    rect(canvx * 0.18, canvy * 0.18, color)

    color = '#F7F795'
    turtle.goto(-canvx * 0.34, -canvy * 0.05)
    rect(canvx * 0.05, canvy * 0.05, color)
    turtle.goto(-canvx * 0.16, canvy * 0.3)
    rect(canvx * 0.05, canvy * 0.05, color)
    turtle.goto(-canvx * 0.16, canvy * 0.23)
    rect(canvx * 0.05, canvy * 0.05, color)
    turtle.goto(-canvx * 0.1, -canvy * 0.2)
    rect(canvx * 0.05, canvy * 0.05, color)
    turtle.goto(-canvx * 0.03, canvy * 0.1)
    rect(canvx * 0.05, canvy * 0.05, color)
    turtle.goto(canvx * 0.22, canvy * 0.05)
    rect(canvx * 0.05, canvy * 0.05, color)
    turtle.pendown()


canvx = 660
canvy = 660
r = 3
turtle.Screen().setup(canvx, canvy)
turtle.Screen().bgcolor('darkblue')
turtle.speed(0)
turtle.tracer(5, 0)
starsky(r, canvx, canvy)
bilding(canvx, canvy)
positionx = -(canvx // 2)
positiony = 0
turtle.penup()
turtle.goto(positionx, 0)
turtle.pendown()