L = list(map(set, input().split()))
print('YES' if min(L[0] == l for l in L) else 'NO')
