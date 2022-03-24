list = []
for i in range(int(input())):
    s = input()
    a = s.find('a')
    n1 = s.find('n', a)
    t = s.find('t', n1)
    o = s.find('o', t)
    n2 = s.find('n', o)
    if a < n1 < t < o < n2:
        list.append(i + 1)
print(*list)
