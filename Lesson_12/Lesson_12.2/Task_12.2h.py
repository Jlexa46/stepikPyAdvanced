def generate_password(length):
    import random
    import string
    s_digits = set(string.digits) - set('0') - set('1')
    s_lower = set(string.ascii_lowercase) - set('l') - set('o')
    s_upper = set(string.ascii_uppercase) - set('I') - set('O')

    l1 = random.randint(1, length - 2) if length < len(s_digits) else random.randint(1, len(s_digits) - 1)
    l2 = random.randint(1, length - l1 - 1)
    l3 = length - l1 - l2

    psw = set(random.sample(s_digits, l1))
    psw |= set(random.sample(s_upper, l2))
    psw |= set(random.sample(s_lower, l3))

    random.shuffle(list(psw))
    return ''.join(psw)


def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))


n, m = int(input()), int(input())
generate_passwords(n, m)
