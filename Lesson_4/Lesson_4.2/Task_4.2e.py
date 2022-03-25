list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = sum([sum(_) for _ in list1])
counter = sum([len(_) for _ in list1])

print(total / counter)
