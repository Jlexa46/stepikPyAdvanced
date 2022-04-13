n = int(input())
z1, z2 = [complex(input()) for _ in range(2)]
print((z1 ** n) + (z2 ** n) + (z1.conjugate() ** n) + (z2.conjugate() ** (n+1)))
