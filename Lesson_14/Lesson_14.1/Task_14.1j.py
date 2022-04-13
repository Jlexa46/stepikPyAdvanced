import turtle


def union_star(side):
  for _ in range(5):
    turtle.forward(side)
    turtle.right(144)


union_star(200)
