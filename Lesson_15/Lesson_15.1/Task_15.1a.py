def matrix(n=1, m=None, value=0):
    if m is None:
        m = n
    return [[value] * m] * n
