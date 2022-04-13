import turtle

turtle.pencolor('red')
turtle.dot()
for i in range(-9, 9, 2):
    turtle.pendown()
    turtle.pencolor('lightblue')
    turtle.goto(25 + i * 10, -150)
    turtle.pencolor('blue')
    turtle.dot()
    turtle.penup()
    turtle.goto(0, 0)
