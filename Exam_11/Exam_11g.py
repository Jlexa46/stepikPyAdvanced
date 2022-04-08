def merge(values):      # values - это список словарей
    _dict = {}
    for d in values:
        for key,value in d.items():
            if key not in _dict:
                _dict[key] = {value}
            else:
                _dict[key].update({value})
    return _dict
