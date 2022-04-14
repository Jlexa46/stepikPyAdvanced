import turtle

def sq(side, color):
  turtle.fillcolor(color)
  turtle.begin_fill()
  for i in range(4):
    turtle.forward(side)
    turtle.right(90)
  turtle.end_fill()

side = 50
n = 8
canvx = 400
canvy = 400
turtle.Screen().setup(canvx, canvy)
turtle.speed(0)
positionx = -(canvx // 2)
positiony = canvy // 2
turtle.penup()
turtle.goto(positionx, positiony)
turtle.pendown()
colors = ['black', 'white']
for j in range(n):
  for i in range(n):
    sq(side, colors[(i + j)% 2])
    turtle.forward(side)
  positiony -= side
  turtle.penup()
  turtle.goto(positionx, positiony)
  turtle.pendown()