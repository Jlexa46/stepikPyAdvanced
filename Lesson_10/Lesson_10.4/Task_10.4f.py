_dict = {}
for _ in range(int(input())):
    _line = input().split()
    _dict[_line[1].lower()] = _dict.get(_line[1].lower(), '') + ' ' + _line[0]
[print(_dict.get(input().lower(), 'абонент не найден')) for _ in range(int(input()))]
