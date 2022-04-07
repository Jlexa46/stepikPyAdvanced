_dict = {}
for _ in range(int(input())):
    _line = input().split()
    for i in range(1, len(_line)):
        _dict[_line[i]] = _line[0]
[print(_dict[input()]) for _ in range(int(input()))]
