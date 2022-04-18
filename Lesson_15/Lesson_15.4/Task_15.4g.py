def comparator(__num):
    return sum(map(int, __num))


_list = [el for el in input().split()]
_list.sort(key=comparator)
print(*_list)
