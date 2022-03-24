lst = [int(input()) for _ in range(int(input()))]
number = int(input())
is_find = False
for i in range(len(lst)):
    for j in range(len(lst)):
        if i == j:
            continue
        if lst[i] * lst[j] == number:
            is_find = True
            break
print('ДА' if is_find else 'НЕТ')
