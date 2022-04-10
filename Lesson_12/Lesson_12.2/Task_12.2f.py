import random
storage = {n for n in range(1, 70)}
for i in range(5):
    row = random.sample(storage, 5)
    storage -= set(row)
    if i == 2:
        row[2] = 0
    print(*row)
