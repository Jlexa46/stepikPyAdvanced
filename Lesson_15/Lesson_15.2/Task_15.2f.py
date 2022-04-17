def info_kwargs(**kwargs):
    [print(str(key) + ': ' + str(value)) for key,value in sorted(kwargs.items())]
