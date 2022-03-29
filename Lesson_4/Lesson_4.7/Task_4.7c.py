n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = a[:]
m = int(input())

for _ in range(m - 1):
    c = [[1] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            row = []
            for k in range(n):
                row.append(b[i][k] * a[k][j])
            c[i][j] = sum(row)
    b = c

[print(*[b[i][j] for j in range(n)]) for i in range(n)]
