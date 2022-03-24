list = [int(i) for i in input().split()]
last = list[-1]
for i in range(len(list) - 1, 0, -1):
    list[i] = list[i - 1]
list[0] = last
print(*list)
