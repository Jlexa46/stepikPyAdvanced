import turtle, random

turtle.speed(0)
turtle.Screen().bgcolor('black')
turtle.up()
def star(x, y):
    turtle.goto(x, y)
    turtle.left(random.randint(0, 360))
    s = random.choice(['red', 'blue', 'green', 'yellow', 'purple', 'white'])
    turtle.fillcolor(s)#(tuple(random.randint(0, 255) for _ in '123'))
    side = random.randint(5, 20)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(side)
        turtle.right(144)
    turtle.end_fill()

def mouse_click(x, y):
    star(x, y)

turtle.Screen().onclick(mouse_click)
turtle.Screen().listen()