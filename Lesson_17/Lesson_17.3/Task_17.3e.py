with open('nums.txt', 'rt', encoding='utf-8') as file:
    lines = file.readlines()
nums = []
for line in lines:
    s = ''
    for l in line:
        s += l if l in '0123456789' else ' '
    nums.extend(s.split())
print(sum(map(int, nums)))
