s, n = input().split(), int(input())
lst = [[] for _ in range(n)]
counter = 0
for i in range(len(s)):
    lst[counter].extend(s[i])
    counter = 0 if counter == n - 1 else counter + 1
print(lst)
