n, matrix, maximum = int(input()), [], -51
for i in range(n):
    matrix.append(list(map(int, input().split())))
    maximum = max(maximum, *[matrix[i][j] for j in range(n) if i >= j])
print(maximum)
