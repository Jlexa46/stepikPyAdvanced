with open('goats.txt', 'rt', encoding='utf-8') as file:
    total = 0
    _dict = {}
    line = file.readline().strip()
    while line != 'GOATS':
        line = file.readline().strip()
    for line in file:
        key = file.readline().strip()
        _dict[key] = _dict.get(key, 0) + 1
        total += 1

with open('answer.txt', 'wt', encoding='utf-8') as file:
    for line in filter(lambda x: int(_dict[x] / total*100) > 7, sorted(_dict)):
        file.write(line + '\n')
