n, m = [int(input()) for _ in range(2)]
answer = len({input() for _ in range(n)}.symmetric_difference({input() for _ in range(m)}))
print('NO' if answer == 0 else answer)
