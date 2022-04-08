_dict, operand = {}, {'write': 'W', 'read': 'R', 'execute': 'X'}
for _ in range(int(input())):
    text = input().split()
    _dict[text[0]] = [text[i] for i in range(1, len(text))]

for _ in range(int(input())):
    text = input().split()
    print('OK' if operand[text[0]] in _dict[text[1]] else 'Access denied')
