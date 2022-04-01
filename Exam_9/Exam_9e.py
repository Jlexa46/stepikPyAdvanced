s1 = {int(c) for c in input().split()}
s2 = {int(c) for c in input().split()}
if len(s1 & s2) > 0: print(*sorted(s1 & s2, reverse=True))
else: print("BAD DAY")
