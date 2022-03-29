n = int(input())
magic_square = [list(map(int, input().split())) for _ in range(n)]
dict = [i for i in range(1, (n ** 2) + 1)]
is_magic_square = True
for i in range(n):
    sum_1 = sum_2 = 0
    for j in range(n):
        if magic_square[i][j] in dict:
            dict.remove(magic_square[i][j])
        sum_1 += magic_square[i][j]
        sum_2 += magic_square[j][i]
    is_magic_square *= sum_1 == sum_2
print('YES' if len(dict) == 0 and is_magic_square else 'NO')
