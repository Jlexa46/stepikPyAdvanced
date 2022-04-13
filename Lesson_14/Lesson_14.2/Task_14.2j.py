import turtle

diametr = 25

for i in range(5):
  turtle.pencolor(['blue', 'black', 'red', 'green', 'yellow'][i])
  turtle.pendown()
  turtle.circle(diametr)
  turtle.penup()
  if i == 2:
    turtle.left(90)
    turtle.forward(diametr)
    turtle.left(90)
    turtle.forward(diametr)
  else:
    turtle.forward(diametr*2)
