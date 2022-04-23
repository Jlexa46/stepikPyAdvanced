from functools import reduce
with open('numbers.txt', 'rt', encoding='utf-8') as file:
    for line in file:
        print(reduce(lambda x, y: x + int(y), filter(lambda x: x != '', line.strip().split()), 0))
