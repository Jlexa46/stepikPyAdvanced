def chunked(_list, _num):
    lst = []
    if len(_list) < _num:
        lst.append(_list)
        return lst
    for i in range(_num, len(_list) + 1, _num):
        lst.append(_list[i-_num:i])
    tail = len(_list) % _num
    if tail > 0:
        lst.append(_list[len(_list)-tail:len(_list)])
    return lst


print(chunked(input().split(), int(input())))

# modified
# def chunked(_list, _num):
#     return [_list[i:i+_num] for i in range(0, len(_list), _num)]
# print(chunked(input().split(), int(input())))
