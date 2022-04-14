import turtle

turtle.speed(0)

turtle.begin_fill()
turtle.goto(25,0)
turtle.goto(25,75)
turtle.goto(-25,75)
turtle.goto(-25,-75)
turtle.goto(25,-75)
turtle.goto(25,0)
turtle.end_fill()

turtle.goto(0,25)
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.goto(0,-25)
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.goto(0,-75)
turtle.fillcolor('green')
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()