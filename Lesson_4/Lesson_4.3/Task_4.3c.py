def pascal_triangle(row):
    new_row = [1]
    if len(row) == 1:
        new_row = [1, 1]
    else:
        for i in range(1, len(row)):
            new_row.append(row[i-1] + row[i])
        new_row.append(1)
    return new_row


row = [1]
for i in range(int(input())):
    row = pascal_triangle(row)
print(row)
