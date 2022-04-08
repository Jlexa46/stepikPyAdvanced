import random
n = int(input())    # количество попыток
[print('Орел' if random.randint(0, 2) else 'Решка') for _ in range(n)]
