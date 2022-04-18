from math import sin, sqrt


def square(x):
    return x**2


def cube(x):
    return x**3


num = int(input())
print({'квадрат': square, 'куб': cube, 'корень': sqrt, 'модуль': abs, 'синус': sin}[input()](num))
