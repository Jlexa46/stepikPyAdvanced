n,  matrix = int(input()), []
for i in range(n):
    matrix.append(list(map(int, input().split())))

is_symmetry = min([matrix[i][j] == matrix[j][i] for i in range(n) for j in range(n)])

if is_symmetry:
    print('YES')
else:
    print('NO')
