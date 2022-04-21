print('YES' if all([any([input().split()[1] == '5' for __ in range(int(input()))]) for _ in range(int(input()))]) else 'NO')
