_list = input().split()
for el in set(_list):
    count = -1
    for i in range(len(_list)):
        count = count + 1 if _list[i] == el else count
        _list[i] = _list[i] + '_' + str(count) if _list[i] == el and count >= 1 else _list[i]
print(*_list)
