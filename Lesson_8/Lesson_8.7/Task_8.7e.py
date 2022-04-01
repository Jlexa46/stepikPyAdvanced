s1, s2, s3 = [set(map(int, input().split())) for _ in range(3)]
print(*sorted(s3 - (s1 | s2), reverse=True))
