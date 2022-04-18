athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]


def comparator_1(_tuple):
        return _tuple[0]


def comparator_2(_tuple):
        return _tuple[1]


def comparator_3(_tuple):
        return _tuple[2]


def comparator_4(_tuple):
        return _tuple[3]


athletes.sort(key={'1': comparator_1, '2': comparator_2, '3': comparator_3, '4': comparator_4}[input()])
[print(*a) for a in athletes]
