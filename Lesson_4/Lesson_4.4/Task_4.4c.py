n, matrix, total = int(input()), [], 0
for i in range(n):
    matrix.append(input().split())
    total += int(matrix[i][i])
print(total)

