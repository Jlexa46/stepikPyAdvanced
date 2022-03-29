n, m = map(int, input().split())
lst = [[0] * m for i in range(n)]
counter, low_h, low_v, hight_h, hight_v = 1, 0, 0, m, n

while True:
    for j in range(low_h, hight_h - 1):
        if counter > n * m: break
        lst[low_v][j], counter = counter, counter + 1
    if low_h == hight_h - 1 and n == m:
        lst[low_v][low_h] = counter
        break
    if counter > n * m: break

    for i in range(low_v, hight_v - 1):
        if counter > n * m: break
        lst[i][hight_h - 1], counter = counter, counter + 1
    if counter > n * m: break

    for j in range(hight_h - 1, low_h, -1):
        if counter > n * m: break
        lst[hight_v - 1][j], counter = counter, counter + 1
    if counter > n * m: break

    for i in range(hight_v - 1, low_v, -1):
        if counter > n * m: break
        lst[i][low_h], counter = counter, counter + 1
    if counter > n * m: break

    low_h, low_v, hight_h, hight_v = low_h + 1, low_v + 1, hight_h - 1, hight_v - 1

[print(*[str(lst[i][j]).ljust(3) for j in range(m)]) for i in range(n)]
