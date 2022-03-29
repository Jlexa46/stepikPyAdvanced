n, m = map(int, input().split())
[print(*[m * i + j + 1 for j in range(m)]) for i in range(n)]
