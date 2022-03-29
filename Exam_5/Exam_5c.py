n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
[print(*[lst[j][i] for j in range(n)]) for i in range(n)]
