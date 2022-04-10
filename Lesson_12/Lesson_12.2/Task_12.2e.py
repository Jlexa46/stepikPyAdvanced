import random
x = [c for c in input()]
random.shuffle(x)
print(*x, sep='')
