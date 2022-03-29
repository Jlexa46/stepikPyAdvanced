n, m = map(int, input().split())
[print(*[(m * i + 1 + j) if i % 2 == 0 else m * (i + 1) - j for j in range(m)]) for i in range(n)]

