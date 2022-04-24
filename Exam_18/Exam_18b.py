total = 0
with open('ledger.txt', 'rt', encoding='utf-8') as file:
    for line in file:
        total += int(line[1:].strip())
print('$', total, sep='')
