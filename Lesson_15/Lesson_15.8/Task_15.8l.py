def evaluate(__coefficients, __x):
    from functools import reduce
    return reduce(lambda _x, _y: _x + _y, map(lambda _x, _y: _x * __x ** _y, __coefficients, range(len(__coefficients))[::-1]))


coefficients = list(map(int, input().split()))
x = int(input())

print(evaluate(coefficients, x))
