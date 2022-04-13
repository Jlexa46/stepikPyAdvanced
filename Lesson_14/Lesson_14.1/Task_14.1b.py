import turtle


def triangle(side):
  turtle.right(60)
  for _ in range(3):
    turtle.forward(side)
    turtle.right(120)


triangle(int(input()))
