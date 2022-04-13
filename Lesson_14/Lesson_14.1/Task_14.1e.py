import turtle


def hexagon(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)


hexagon(int(input))
