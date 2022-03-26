n, m = int(input()), int(input())
matrix = []
for i in range(n):
    matrix.append([input() for _ in range(m)])

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
