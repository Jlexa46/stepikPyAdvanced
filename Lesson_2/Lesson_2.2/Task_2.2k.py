s = (input() + ' запретил букву').split()
next_char = ord('а')
while chr(next_char) != 'ѐ':
    _s = str(s)
    if chr(next_char) not in _s:
        next_char += 1
        continue
    print(*s, chr(next_char))
    for i in range(len(s)):
        s[i] = s[i].replace(chr(next_char), '')
    if '' in s: s.remove('')
    next_char += 1
