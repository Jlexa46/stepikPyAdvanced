abscissas = [float(num) for num in input().split()]
ordinates = [float(num) for num in input().split()]
applicates = [float(num) for num in input().split()]

print(all(map(lambda x: x[0]**2 + x[1]**2 + x[2]**2 <= 2**2, zip(abscissas, ordinates, applicates))))
