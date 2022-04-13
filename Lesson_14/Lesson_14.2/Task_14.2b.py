import turtle

for _ in range(4):
  turtle.forward([100, 50][_%2])
  turtle.right(90)
  turtle.pensize(10)
  turtle.dot()
  turtle.pensize(1)