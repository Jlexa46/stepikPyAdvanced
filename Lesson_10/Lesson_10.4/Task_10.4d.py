_dict = dict([(input().split()) for _ in range(int(input()))])
_dict.update(dict([(_dict[d], d) for d in _dict]))
print(_dict[input()])
