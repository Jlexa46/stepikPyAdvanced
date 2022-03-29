n = int(input())
[print(*[1 if i == j or j == n - i - 1 else 0 for j in range(n)]) for i in range(n)]
