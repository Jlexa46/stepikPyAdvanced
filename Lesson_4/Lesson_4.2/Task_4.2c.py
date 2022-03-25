list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1

for l in list1:
    m = max(l)
    if maximum <= m:
        maximum = m

print(maximum)


# modified
# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# maximum = max([max(l) for l in list1])
# print(maximum)
