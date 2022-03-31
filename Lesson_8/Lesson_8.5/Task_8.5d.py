l, s = input().split(), set()
for el in l:
    _s = s.copy()
    s.add(int(el))
    print('YES' if _s == s else 'NO')

