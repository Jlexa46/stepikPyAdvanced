n, m, matrix = int(input()), int(input()), []
maximum, max_i, max_j = -100, 10, 10
for i in range(n):
    matrix.append(list(map(int, input().split())))
    for j in range(m):
        if maximum < matrix[i][j]:
            maximum, max_i, max_j = matrix[i][j], i, j
print(max_i, max_j)
