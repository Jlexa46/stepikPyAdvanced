from fractions import Fraction as F
from math import factorial as f
print(sum([F(1, f(i)) for i in range(1, int(input())+1)]))
