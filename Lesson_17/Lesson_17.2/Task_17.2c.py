import random

file = open('lines.txt', 'rt')
lists = list(map(str.rstrip, file.readlines()))
file.close()
print(*random.sample(lists, 1))
