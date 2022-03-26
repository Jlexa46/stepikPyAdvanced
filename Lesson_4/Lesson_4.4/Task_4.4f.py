n, matrix, maximum = int(input()), [], -51
for i in range(n):
    matrix.append(list(map(int, input().split())))
    for j in range(n):
        if i >= j and i <= n-1-j or i <= j and i >= n-1-j:
            maximum = max(maximum, matrix[i][j])
print(maximum)
