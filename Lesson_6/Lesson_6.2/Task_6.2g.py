numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
M, m = numbers[0], numbers[0]
for i in range(len(numbers)):
    M = numbers[i] if M < numbers[i] else M
    m = numbers[i] if m > numbers[i] else m
print(M + m)
