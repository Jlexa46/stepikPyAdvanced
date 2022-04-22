from functools import reduce
file = open('nums.txt', 'rt')
print(reduce(lambda total, x: total + int(x), file.read().split(), 0))
file.close()
