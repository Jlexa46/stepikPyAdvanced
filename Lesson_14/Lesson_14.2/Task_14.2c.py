import turtle


def web(length, count):
  for _ in range(count):
    turtle.forward(length)
    turtle.shape('triangle')
    turtle.stamp()
    turtle.shape('turtle')
    turtle.backward(length)
    turtle.right(360/count)


web(150, 10)
