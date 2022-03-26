def exchange_columns(matrix, col1, col2):
    for i in range(len(matrix)):
        matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]
    return matrix

n, m, matrix = int(input()), int(input()), []
for i in range(n):
    matrix.append(list(map(int, input().split())))

columns = list(map(int, input().split()))
matrix = exchange_columns(matrix, columns[0], columns[1])

for row in matrix:
    for el in row:
        print(el, end=' ')
    print()
