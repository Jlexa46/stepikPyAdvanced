_temp = input().split()
for i in range(len(_temp)):
    _temp[i] = _temp[i].lower()
    for char in '.,:;-?!':
        _temp[i] = _temp[i].replace(char, '')
print(len(set(_temp)))
