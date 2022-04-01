s = set()
for _ in range(int(input())):
    if s == set():
        s = {input() for __ in range(int(input()))}
        continue
    t = {input() for __ in range(int(input()))}
    s.intersection_update(t)
print(*sorted(s), sep='\n')

# modified
# print(*sorted(set.intersection(*[{input() for _ in range(int(input()))} for _ in range(int(input()))])), sep = '\n')
