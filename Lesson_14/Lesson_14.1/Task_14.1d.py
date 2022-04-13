import turtle


def square(side):
    for _ in range(4):
        turtle.right(90)
        turtle.forward(side)


def squares(side):
    for _ in range(4):
        square(side)
        turtle.left(90)

    turtle.left(45)
    for _ in range(4):
        square(side)
        turtle.left(90)


squares(int(input()))
