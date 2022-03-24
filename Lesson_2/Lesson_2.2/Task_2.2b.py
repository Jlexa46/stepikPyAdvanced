list = [int(i) for i in input().split()]
count = 0
for i in range(1, len(list)):
    count += 1 if list[i - 1] < list[i] else 0
print(count)
