s1, s2 = set(input().split()), set(input().split())
print(len((s1 | s2) - (s1 - s2) - (s2 - s1)))
