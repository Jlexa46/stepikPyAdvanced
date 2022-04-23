with open('file.txt', 'rt', encoding='utf-8') as file:
    lines = file.readlines()

print('Input file contains:')
print(sum([1 for line in lines for c in line if c.isalpha()]), 'letters')
print(sum(map(lambda x: len(x.split()), lines)), 'words')
print(len(lines), 'lines')
