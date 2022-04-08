import random
length = int(input())    # длина пароля
_set = [chr(c) for c in range(65, 91)] + [chr(c) for c in range(97, 123)]
print(*[_set[random.randint(0, len(_set)-1)] for _ in range(length)], sep='')
