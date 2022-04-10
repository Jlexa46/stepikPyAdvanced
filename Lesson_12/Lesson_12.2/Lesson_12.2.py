# Метод shuffle()
# Метод shuffle() принимает список в качестве обязательного аргумента и перемешивает его случайным образом.

# Следующий код перемешивает список numbers случайным образом, а затем выводит его содержимое:
import random
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)
print(numbers)  # [4, 7, 8, 1, 2, 3, 6, 5]


# Метод choice()
# Метод choice() принимает список (строку, кортеж) в качестве обязательного аргумента и возвращает один случайный элемент.

# Следующий код выводит по одному случайному элементу из строки 'BEEGEEK', списка [1, 2, 3, 4] и кортежа
# ('a', 'b', 'c', 'd'):
import random
print(random.choice('BEEGEEK'))
print(random.choice([1, 2, 3, 4]))
print(random.choice(('a', 'b', 'c', 'd')))


# Метод sample()
# Метод sample() принимает два обязательных аргумента: первый – список (строка, кортеж, множество), второй – количество
# случайных элементов. Возвращает список из указанного количества уникальных (имеющих разные индексы) случайных
# элементов.
import random
numbers = [2, 5, 8, 9, 12]
print(random.sample(numbers, 1))
print(random.sample(numbers, 2))
print(random.sample(numbers, 3))
print(random.sample(numbers, 5))

# Количество случайных элементов не должно превышать длину исходного списка (строки).


# Модуль string
# Встроенный модуль string раньше использовался для расширения стандартных возможностей (функционала) строкового типа
# данных str. На текущий момент все функции из модуля string переехали в методы строкового типа данных str, однако в
# модуле string остались удобные константные строки, которые можно использовать при решении задач.
import string
print(string.ascii_letters)     # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_uppercase)   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)   # abcdefghijklmnopqrstuvwxyz
print(string.digits)            # 0123456789
print(string.hexdigits)         # 0123456789abcdefABCDEF
print(string.octdigits)         # 01234567
print(string.punctuation)       # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.printable)         # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ \t\n\r\x0b\x0c


# Примечания
# Примечание 1. Помимо рассмотренных в уроке методов, модуль random содержит много дополнительных методов.
# Подробнее о модуле random можно почитать в документации.
# https://docs.python.org/3/library/random.html#
