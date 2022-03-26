n, matrix = int(input()), []
for i in range(n):
    matrix.append(input().split())
    average = sum([int(el) for el in matrix[i]]) // n
    count = 0
    for j in range(n):
        count += 1 if int(matrix[i][j]) > average else 0
    print(count)

