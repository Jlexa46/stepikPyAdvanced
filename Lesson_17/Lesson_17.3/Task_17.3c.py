with open('lines.txt', 'rt', encoding='utf-8') as file:
    lines = list(map(str.strip, file.readlines()))
max_length = max(lines, key=len)
print(*filter(lambda x: (len(x) == len(max_length)), lines), sep='\n')
