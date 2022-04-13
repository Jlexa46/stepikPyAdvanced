import turtle

turtle.Screen().bgcolor('cyan')
turtle.shape('turtle')
for _ in range(12):
  turtle.penup()
  turtle.forward(110)
  turtle.pendown()
  turtle.forward(20)
  turtle.penup()
  turtle.forward(20)
  turtle.stamp()
  turtle.backward(150)
  turtle.right(360/12)
