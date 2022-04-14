import turtle

turtle.speed(10)
sides = [('Восток', False, 'left', ('Arial', 8, 'normal')),
         ('Север', False, 'center', ('Arial', 8, 'normal')),
         ('Запад', False, 'right', ('Arial', 8, 'normal')),
         ('Юг', False, 'center', ('Arial', 8, 'normal'))]

turtle.circle(20)
turtle.goto(0, 20)

for side in sides:
  turtle.forward(70)
  turtle.penup()
  turtle.forward(15)
  turtle.write(*side)
  turtle.backward(85)
  turtle.left(90)
  turtle.pendown()