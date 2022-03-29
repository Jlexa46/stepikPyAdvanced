n = int(input())
for i in range(n):
    for j in range(n):
        if i == j or j == n - 1 - i or i == n // 2 or j == n // 2:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()

# modified
# [print(*['.*'[len({i, j, n-j-1, n//2}) < 4] for j in range(n)]) for n in [int(input())] for i in range(n)]
