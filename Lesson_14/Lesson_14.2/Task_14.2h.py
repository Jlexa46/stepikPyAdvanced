import turtle


def triangle(side):
  turtle.right(60)
  for _ in range(3):
    turtle.forward(side)
    turtle.right(120)


def double(side):
  triangle(side)
  turtle.right(30)
  turtle.penup()
  turtle.forward(170)
  turtle.right(90)
  turtle.pendown()
  triangle(side)


turtle.speed(10)
double(150)
