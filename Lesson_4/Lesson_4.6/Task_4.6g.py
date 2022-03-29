n, m = map(int, input().split())
[print(*[j for j in range(i % m if i % m > 0 else m, m + 1)] + [k for k in range(1, i % m if i % m > 0 else m)]) for i in range(1, n + 1)]
