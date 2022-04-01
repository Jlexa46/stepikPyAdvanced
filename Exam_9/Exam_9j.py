n, m = int(input()), int(input())
counter, s = 0, []
for _ in range(n + m):
    t = input()
    if t in s:
        counter -= 1
        s.remove(t)
        continue
    else:
        counter += 1
        s.append(t)
print('NO' if counter == 0 else counter)

# modified
# n = int(input()) + int(input())
# print(2 * len(set([input() for _ in range(n)])) - n or 'NO')