import turtle


def square(side):
  for _ in range(4):
    turtle.right(90)
    turtle.forward(side)


def squares(side, angle):
  turtle.left((90 + angle))
  for _ in range(3):
    square(side)
    turtle.left(angle/2)


squares(int(input()), 45)