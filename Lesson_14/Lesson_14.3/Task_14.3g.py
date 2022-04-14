import turtle
turtle.Screen().bgcolor('blue')
moon = turtle.Turtle()
moon.hideturtle()
moon.pencolor('orange')
moon.dot(200)
shadow = {0: turtle.Turtle(), 5: turtle.Turtle()}
for i in [0, 5]:
  shadow[i].hideturtle()
  shadow[i].pencolor('blue')
  shadow[i].penup()
while 1:
  for i in range(200, -201, -5):
    shadow[i % 10].goto(i, 0)
    shadow[i % 10].dot(200)
    shadow[(i + 5) % 10].clear()