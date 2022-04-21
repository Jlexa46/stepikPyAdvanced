def check_ip(__s):
    return all(map(lambda x: (set(x).difference('0123456789') == set()) and ((x[1] in '012345' and x[2] in '012345') if (len(x) == 3) else len(x) <= 3), ['0' if len(b.lstrip('0')) == 0 else b.lstrip('0') for b in __s.split('.')]))


print(check_ip(input()))

#modified
print(all(x.isdigit() and int(x) < 256 for x in input().split('.')))
