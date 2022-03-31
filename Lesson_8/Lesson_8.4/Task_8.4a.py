numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
M = m = list(numbers)[0]
for n in numbers:
    M = n if n > M else M
    m = n if n < m else m
print(M + m)
