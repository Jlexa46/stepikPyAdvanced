import turtle


def star(radius):
    for _ in range(12):
        turtle.forward(radius)
        turtle.backward(radius)
        turtle.right(30)


star(100)
