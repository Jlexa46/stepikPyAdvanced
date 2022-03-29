position = input()
position = [ord(position[0]) - 97, 8 - int(position[1])]

for i in range(8):
    for j in range(8):
        if j == position[0] and i == position[1]:
            print('Q', end=' ')
        elif j == position[0] or i == position[1] or position[0] - j == i - position[1] or -position[1] - j == -position[0] - i:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()
