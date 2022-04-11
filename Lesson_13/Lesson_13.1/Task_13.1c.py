from decimal import *
num = Decimal(input())
s = set(str(num)) - {'.'} - {'-'}
print(int(min(s)) + int(max(s)))
