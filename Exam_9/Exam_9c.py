l = [input() for _ in range(int(input())+1)]
print('OK' if len(l) == len(set(l)) else 'REPEAT')
