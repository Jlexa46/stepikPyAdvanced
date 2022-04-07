_dict = {}
for _ in range(int(input())):
    _line = input().split(': ')
    _dict[_line[0].lower()] = _line[1]
[print(_dict.get(input().lower(), 'Не найдено')) for _ in range(int(input()))]


# modified
# _dict = {key.lower(): value for _ in range(int(input())) for key, value in [input().split(': ', 1)]}
# print(*(_dict.get(input().lower(), 'Не найдено') for _ in range(int(input()))), sep='\n')
