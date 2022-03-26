n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(-1, -n-1, -1):
        print(matrix[j][i], end=' ')
    print()
