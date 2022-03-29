n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
maximum = lst[n-1][n-1]
for i in range(n):
    for j in range(n):
        if i <= j >= n - i - 1 or i >= j >= n - i - 1:
            maximum = max(maximum, lst[i][j])
print(maximum)
