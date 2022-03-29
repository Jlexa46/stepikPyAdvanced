n = int(input())
for i in range(n):
    for j in range(n):
        if j > n - i - 1:
            print(2, end=' ')
        elif j < n - i - 1:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()

# modified
# n = int(input())
[print(*[(i > (n - j - 1)) + int(i >= (n - j - 1)) for j in range(n)]) for i in range(n)]
