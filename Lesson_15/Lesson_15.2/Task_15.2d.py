def greet(name, *args):
    return 'Hello, ' + ' and '.join((name, *args)) + '!'
