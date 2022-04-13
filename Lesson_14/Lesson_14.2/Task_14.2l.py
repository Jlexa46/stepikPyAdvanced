import turtle

def flake(x, y, size):
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  for k in range(8):
    turtle.right(45)
    for i in range(4):
      turtle.left(45)
      turtle.forward(size)
      turtle.backward(size)
      turtle.right(90)
      turtle.forward(size)
      turtle.backward(size)
      turtle.left(45)
      turtle.forward(size)
    turtle.goto(x, y)
  turtle.penup()


turtle.speed(0)

flake(0,0, 5)