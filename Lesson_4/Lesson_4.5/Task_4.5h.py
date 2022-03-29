board = [['.'] * 8 for _ in range(8)]
position = input()
position = [(ord(position[0]) - 97), int(position[1]) - 1]
board[position[1]][position[0]] = 'N'
for i in range(7, -1, -1):
    for j in range(8):
        if abs(position[1] - i) == 2 and abs(position[0] - j) == 1:
            board[i][j] = '*'
        if abs(position[1] - i) == 1 and abs(position[0] - j) == 2:
            board[i][j] = '*'
        print(board[i][j], end=' ')
    print()
