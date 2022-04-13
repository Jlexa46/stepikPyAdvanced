import turtle


def rhomb(width, height):
  for side in range(4):
    turtle.forward([width, height][side%2])
    turtle.right([60, 120][side%2])


rhomb(int(input()), int(input()))
