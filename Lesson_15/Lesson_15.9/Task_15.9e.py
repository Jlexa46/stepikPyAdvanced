print(*filter(lambda x: all([x % int(n) == 0 for n in str(x)]), [num for num in range(int(input()), int(input())) if str(num).count('0') == 0]))
