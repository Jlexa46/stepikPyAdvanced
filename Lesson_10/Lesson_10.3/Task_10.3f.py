s = input().lower()
for c in '.,!?:;-':
    if c in s:
        s = s.replace(c, '')
s = s.split()
_dict = dict([(word, s.count(word)) for word in set(s)])
print(sorted([key for key, value in _dict.items() if value == min(list(_dict.values()))])[0])
