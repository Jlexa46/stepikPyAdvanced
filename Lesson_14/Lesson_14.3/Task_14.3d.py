import turtle


def rainbow_circle(radius):
    """draws rainbow circle of custom size"""

    colors = ("#FF0000", "#FFA600", "#FFFF00", "#62FF00", "#89F590", "#69C5FF",
              "#1E56FC", "#4800FF", "#CC00FF", "#FF5099")
    turtle.hideturtle()

    for i in range(10):
        turtle.dot(radius - (radius / 10) * i, colors[i])


rainbow_circle(300)