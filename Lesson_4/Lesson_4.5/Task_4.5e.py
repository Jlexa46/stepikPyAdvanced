n,  matrix = int(input()), []
for i in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    matrix[i][i], matrix[n-1-i][i] = matrix[n-1-i][i], matrix[i][i]

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
