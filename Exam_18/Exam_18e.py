with open(input(), 'rt', encoding='utf-8') as file:
    rows = list(map(lambda x: x.strip(), file.readlines()))

if len(rows) <= 10:
    print(*rows, sep='\n')
else:
    print(*rows[-10:], sep='\n')
