n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    lst[i] = lst[i][::-1]

print('YES' if bool(min([lst[i][j] == lst[j][i] for j in range(-n, 0) for i in range(n)])) else 'NO')
