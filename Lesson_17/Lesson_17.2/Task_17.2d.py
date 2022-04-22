from functools import reduce
file = open('numbers.txt', 'rt')
print(reduce(lambda total, seq: total + int(seq.rstrip()), file.readlines(), 0))
file.close()
