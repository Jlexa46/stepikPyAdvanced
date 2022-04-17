def mean(*args):
    m = [e for e in args if type(e) is int or type(e) is float]
    return sum(m) / len(m) if len(m) > 0 else 0.0
