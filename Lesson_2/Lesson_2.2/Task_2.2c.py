list = [int(i) for i in input().split()]
for i in range(1, len(list), 2):
    list[i - 1], list[i] = list[i], list[i - 1]
print(*list)
