n, m = [int(input()) for _ in range(2)]
print(len({input() for _ in range(n)} - {input() for _ in range(m)}))
