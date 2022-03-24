s = input()
max = count = 0
for c in s:
    if c == 'Р':
        count += 1
    else:
        max = count if max < count else max
        count = 0
max = count if max < count else max
print(max)
