def combination(_list):
    combinates = [[]] + [[c] for c in _list]
    combinator = 2
    if len(_list) == 1:
        return combinates
    while combinator != len(_list):
        for i in range(0, len(_list)):
            sublist = _list[i:i+combinator]
            if sublist not in combinates:
                combinates.append(sublist)
        for i in range(len(_list), 0, -combinator):
            sublist = _list[i:i + combinator]
            if sublist not in combinates:
                combinates.append(sublist)
        combinator += 1
    combinates.append(_list)
    return combinates


print(combination(input().split()))

# modified
# print([[]] + [l[j:i + j + 1] for l in [input().split()] for i in range(len(l)) for j in range(len(l) - i)])
