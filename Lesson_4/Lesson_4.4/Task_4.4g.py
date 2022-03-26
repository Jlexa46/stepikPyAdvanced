n, matrix = int(input()), []
quart_1 = quart_2 = quart_3 = quart_4 = 0
for i in range(n):
    matrix.append(list(map(int, input().split())))
    for j in range(n):
        if i > j and i < n-1-j:
            quart_2 += matrix[i][j]
        elif i < j and i > n-1-j:
            quart_3 += matrix[i][j]
        elif i < j and i < n-1-j:
            quart_1 += matrix[i][j]
        elif i > j and i > n-1-j:
            quart_4 += matrix[i][j]
print(f'Верхняя четверть: {quart_1}\nПравая четверть: {quart_3}\nНижняя четверть: {quart_4}\nЛевая четверть: {quart_2}')
