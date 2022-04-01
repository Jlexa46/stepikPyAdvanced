l = []
for i in range(int(input())):
    l.append(set(input()))
    l[0] = list(set(l[i]) & set(l[0]))
print(*map(int, sorted(l[0])))
