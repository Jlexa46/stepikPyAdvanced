def func_apply(function, __list):
    _list = []
    for element in __list:
        _list.append(function(element))
    return _list

