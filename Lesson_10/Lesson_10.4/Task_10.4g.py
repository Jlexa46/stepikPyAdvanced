cryto_word, _dict = input(), {}
for _ in range(int(input())):
    _line = input().split(': ')
    for s in set(cryto_word):
        if int(_line[1]) == cryto_word.count(s):
            _dict[s] = _line[0]
[print(_dict[c], end='') for c in cryto_word]
