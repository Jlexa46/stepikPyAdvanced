n = int(input())
[print(*[1 if i >= j >= n - i - 1 or i <= j <= n - i - 1 else 0 for j in range(n)]) for i in range(n)]
