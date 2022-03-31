s = set()
for _ in range(int(input())):
    t = set(input().lower())
    for _ in t: s.add(_)
print(len(s))
