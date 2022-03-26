n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

[print(*matrix[i]) for i in range(-1, -len(matrix)-1, -1)]
