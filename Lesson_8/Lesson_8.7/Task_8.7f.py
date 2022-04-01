print(*sorted(set(range(11)) - (set(map(int, input().split())) | set(map(int, input().split())) | set(map(int, input().split())))))
