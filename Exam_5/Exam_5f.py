n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
is_latin_square = True
for i in range(n):
    check_v = [k for k in range(1, n + 1)]
    check_h = [k for k in range(1, n + 1)]
    for j in range(n):
        if lst[i][j] in check_v: check_v.remove(lst[i][j])
        if lst[j][i] in check_h: check_h.remove(lst[j][i])
    is_latin_square *= check_v == [] and check_h == []
print('YES' if is_latin_square else 'NO')
