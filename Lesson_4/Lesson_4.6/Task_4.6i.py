n, m = map(int, input().split())
lst = [[0] * m for i in range(n)]
counter = 0
for q in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if i + j == q:
                counter += 1
                lst[i][j] = counter
[print(*[lst[i][j] for j in range(m)]) for i in range(n)]
