file = open(input(), 'rt')
s1, s2 = '', file.readline().rstrip()
for line in file:
    s1, s2 = s2, line.rstrip()
file.close()
print(s1)
