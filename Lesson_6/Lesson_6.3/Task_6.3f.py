n = int(input())
lst = [input().split() for _ in range(n)]
[print(*lst[i]) for i in range(n)]
print()
[print(*lst[i]) for i in range(n) if lst[i][1] in '45']
