n = int(input())
for i in range(n):
    for j in range(n):
        print(abs(j - i), end=' ')
    print()
