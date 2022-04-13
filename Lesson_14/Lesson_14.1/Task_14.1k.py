import turtle


def square(side):
    for _ in range(4):
        turtle.left(90)
        turtle.forward(side)


def squares(side, d):
    for _ in range(30):
        square(side + d * _)


squares(50, 5)
