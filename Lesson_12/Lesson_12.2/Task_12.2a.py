def generate_ip():
    from random import randint
    return '.'.join([str(randint(0, 255)) for _ in range(4)])
