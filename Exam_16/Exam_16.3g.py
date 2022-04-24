def compose(func_T1, func_T2):
    def func(x):
        return func_T1(func_T2(x))
    return func


def add3(x):
    return x + 3


def mul7(x):
    return x * 7


print(compose(mul7, add3)(1))
print(compose(add3, mul7)(2))
print(compose(mul7, str)(3))
print(compose(str, mul7)(5))
