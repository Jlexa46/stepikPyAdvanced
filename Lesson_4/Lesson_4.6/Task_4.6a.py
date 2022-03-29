n = list(map(int, input().split()))
is_now_dot = True
for i in range(n[0]):
    is_now_dot = not (i % 2 == 1)
    for j in range(n[1]):
        print('.' if is_now_dot else '*', end=' ')
        is_now_dot = not is_now_dot
    print()

# modified
# n, m = map(int, input().split())
# [print(*['.' if (j + i) % 2 == 0 else '*' for j in range(m)]) for i in range(n)]
