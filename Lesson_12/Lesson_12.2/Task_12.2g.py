_c = {input() for _ in range(int(input()))}


def secret_santa(_set):
    import random
    import string
    _class, secret = _set.copy(), dict()
    for student in _set:
        st = random.choice(list(_class))
        if st == student:
            if len(_class) > 1:
                st = random.choice(list(_class))
            else:
                return secret_santa(_set)
        secret[student] = st
        _class -= {st}
    return '\n'.join([key+' - '+value for key, value in secret.items()])


print(secret_santa(_c), sep='\n')


# modified
# import random
# _c = [input() for _ in range(int(input()))]
# random.shuffle(_c)
# for c in range(len(_c)):
#     print(f"{_c[c]} - {_c[(c + 1) % len(_c)]}")
