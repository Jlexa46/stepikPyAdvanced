from functools import reduce
file = open('prices.txt', 'rt')
print(reduce(lambda total, x: total + x, map(lambda x: int(x[1]) * int(x[2]), [line.split('\t') for line in file]), 0))
file.close()
