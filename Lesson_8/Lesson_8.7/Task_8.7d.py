s1, s2, s3 = [list(set(map(int, input().split()))) for _ in range(3)]
for i in sorted(set(s1) | set(s2) | set(s3)):
    print(str(i) + ' ' if (s1.count(i) + s2.count(i) + s3.count(i)) <= 2 else '', end='')
