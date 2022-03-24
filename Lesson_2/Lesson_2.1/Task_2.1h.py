def joseph_problem(number, key):
    num = 0
    for i in range(1, number + 1):
        num = (num + key) % i
    return num + 1


print(joseph_problem(int(input()), int(input())))
