def print_products(*args):
    counter, l = 0, list()
    for i in range(len(args)):
        if type(args[i]) is str:
            if len(args[i]) > 0:
                counter = counter + 1
                l.append(str(counter) + ') ' + args[i])
    print('\n'.join(l) if len(l) > 0 else 'Нет продуктов')
