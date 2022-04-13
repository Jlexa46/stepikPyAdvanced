import turtle

turtle.Screen().bgcolor('lightgreen')
turtle.shape('turtle')
turtle.penup()
for _ in range(50):
  turtle.stamp()
  turtle.forward(_*2)
  turtle.right(20)
