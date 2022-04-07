dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
result = {}
for d in dict2:
    if d in dict1:
        dict2[d] += dict1[d]
result = dict1 | dict2

# modified
# result = {i: dict1.get(i, 0) + dict2.get(i, 0) for i in set(dict1.keys() | dict2.keys())}
