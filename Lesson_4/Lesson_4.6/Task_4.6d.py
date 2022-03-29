n, m = map(int, input().split())
[print(*[n * j + i + 1 for j in range(m)]) for i in range(n)]
