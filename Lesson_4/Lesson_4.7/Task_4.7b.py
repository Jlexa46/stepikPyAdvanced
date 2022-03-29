an, am = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(an)]
input()
bn, bm = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(bn)]

for i in range(an):
    for j in range(bm):
        print(sum([a[i][l] * b[l][j] for l in range(bn)]), end=' ')
    print()
