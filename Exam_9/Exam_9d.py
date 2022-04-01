n, m = [int(input()) for _ in range(2)]
s1 = [input() for _ in range(n)]
s2 = [input() for _ in range(m)]
for s in s2:
    print('YES' if s in s1 else 'NO')
