n, m = int(input()), int(input())
for i in range(n):
    for j in range(m):
        print(str(i * j).ljust(3), end=' ')
    print()

# modified
# [print(*[str(i * j).ljust(3) for j in d[1]]) for d in [[range(int(input())) for _ in 'nm']] for i in d[0]]
