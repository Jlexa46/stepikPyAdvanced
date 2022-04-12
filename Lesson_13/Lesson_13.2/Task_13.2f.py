from math import gcd
num = int(input())
n = m = 0
for i in range(1, num):
    for j in range(i + 1, num):
        if i + j == num and gcd(i, j) == 1:
            n, m = i, j
print(f'{n}/{m}')
