import turtle
turtle.speed(5)

for _ in range(3):
    turtle.forward(90)
    turtle.left(120)

turtle.penup()
turtle.goto(0, 60)

turtle.color('white')
turtle.fillcolor('white')
turtle.begin_fill()
for _ in range(3):
    turtle.forward(90)
    turtle.color('black')
    turtle.dot(30)
    turtle.color('white')
    turtle.right(120)

turtle.end_fill()