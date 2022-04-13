import turtle


def rhomb(width, height):
    for side in range(4):
        turtle.forward([width, height][side % 2])
        turtle.right([60, 120][side % 2])


def rhombs(width, height, count, angle):
    turtle.right(angle)
    for _ in range(count):
        rhomb(width, height)
        turtle.right(angle)


rhombs(60, 80, 10, 35)
