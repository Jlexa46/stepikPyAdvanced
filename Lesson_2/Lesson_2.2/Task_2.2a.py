def quadrants(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return 0


quadrants_1 = quadrants_2 = quadrants_3 = quadrants_4 = 0

for i in range(int(input())):
    coordinates = [int(i) for i in input().split()]
    quad = quadrants(coordinates[0], coordinates[1])
    if quad == 1:
        quadrants_1 += 1
    elif quad == 2:
        quadrants_2 += 1
    elif quad == 3:
        quadrants_3 += 1
    elif quad == 4:
        quadrants_4 += 1

print(f'Первая четверть: {quadrants_1}\nВторая четверть: {quadrants_2}\nТретья четверть: {quadrants_3}\nЧетвертая четверть: {quadrants_4}')
