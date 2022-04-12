from math import gcd
from fractions import Fraction as F
n = int(input())
print(*sorted([F(i, j) for i in range(1, n) for j in range(n, i, -1) if gcd(i, j) == 1]), sep='\n')

