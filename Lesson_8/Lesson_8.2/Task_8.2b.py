n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
_x, _y, _z = n + m - x - t, k + m - y - t, k + n - z - t
_n, _m, _k = n - _x - _z - t, m - _x - _y - t, k - _y - _z - t
print(_n + _m + _k, _x + _y + _z, a - (_n + _m + _k + _x + _y + _z + t), sep='\n')