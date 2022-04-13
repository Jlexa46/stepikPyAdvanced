import turtle

pen = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']

for i in range(52):
  turtle.pencolor(pen[i%6])
  turtle.left(45)
  turtle.forward(i*2+i)
  turtle.pensize(i/2)
