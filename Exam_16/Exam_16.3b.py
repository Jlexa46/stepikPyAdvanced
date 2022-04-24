def product_of_odds(data):   # data - список целых чисел
    from functools import reduce
    return reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 1 ,data), 1)
