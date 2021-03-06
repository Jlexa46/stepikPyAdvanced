# Встроенные функции map(), filter(), reduce()
# Язык Python имеет встроенные реализации функций высшего порядка map(), filter() и reduce() , которые намного удобнее,
# чем наши собственные версии.


# Встроенная функция map()
# Встроенная функция map() имеет сигнатуру map(func, *iterables). В отличие от нашей версии из прошлого урока,
# встроенная функция map() может принимать сразу несколько последовательностей, переменное количество аргументов.

# В качестве параметра func указывается функция, которой будет передаваться текущий элемент последовательности. Внутри
# функции func необходимо вернуть новое значение. Для примера прибавим к каждому элементу списка число 7.
def increase(num):
    return num + 7
numbers = [1, 2, 3, 4, 5, 6]
new_numbers = map(increase, numbers)     # используем встроенную функцию map()
print(new_numbers)                       # <map object at 0x...>

# Такой объект похож на список тем, что его можно перебирать циклом for, то есть итерировать. Такие объекты в Python
# называют итераторами.
def increase(num):
    return num + 7
numbers = [1, 2, 3, 4, 5, 6]
new_numbers = map(increase, numbers)
for num in new_numbers:     # итерируем циклом for
    print(num)              # 8 9 10 11 12 13

# Чтобы получить из итератора список, нужно воспользоваться функцией list():
new_numbers = list(map(increase, numbers))

# Функция map() возвращает объект, поддерживающий итерации, а не список. Чтобы получить из него список, необходимо
# результат передать в функцию list().

# Функции map() можно передать несколько последовательностей. В этом случае в функцию обратного вызова func будут
# передаваться сразу несколько элементов, расположенных в последовательностях на одинаковых позициях.
def func(elem1, elem2, elem3):
    return elem1 + elem2 + elem3
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 20, 30, 40, 50]
numbers3 = [100, 200, 300, 400, 500]
new_numbers = list(map(func, numbers1, numbers2, numbers3))  #  преобразуем итератор в список
print(new_numbers)  # [111, 222, 333, 444, 555]

# Если в последовательностях разное количество элементов, то последовательность с минимальным количеством элементов
# становится ограничителем.
def func(elem1, elem2, elem3):
    return elem1 + elem2 + elem3
numbers1 = [1, 2, 3, 4]
numbers2 = [10, 20]
numbers3 = [100, 200, 300, 400, 500]
new_numbers = list(map(func, numbers1, numbers2, numbers3))  #  преобразуем итератор в список
print(new_numbers)  # [111, 222]

# Встроенная функция map() реализована очень гибко. В качестве последовательностей мы можем использовать: списки,
# строки, кортежи, множества, словари.

# Приведем пример удобного использования встроенной функции map(), которой передано две последовательности.
circle_areas = [3.56773, 5.57668, 4.31914, 6.20241, 91.01344, 32.01213]
result1 = list(map(round, circle_areas, [1]*6))         # округляем числа до 1 знака после запятой
result2 = list(map(round, circle_areas, range(1, 7)))   # округляем числа до 1,2,...,6 знаков после запятой
print(circle_areas)     # [3.56773, 5.57668, 4.31914, 6.20241, 91.01344, 32.01213]
print(result1)          # [3.6, 5.6, 4.3, 6.2, 91.0, 32.0]
print(result2)          # [3.6, 5.58, 4.319, 6.2024, 91.01344, 32.01213]

# Встроенная функция round(x, n=0) принимает два числовых аргумента x и n и округляет переданное число x до n цифр после
# десятичной запятой. Значением по умолчанию для n является 0.

# Встроенная функция filter()
# Встроенная функция filter() имеет сигнатуру filter(func, iterable). В отличие от нашей реализации из прошлого урока
# она может принимать любой итерируемый объект (список, строку, кортеж, и т.д.).

# В качестве параметра func указывается ссылка на функцию, которой будет передаваться текущий элемент
# последовательности. Внутри функции func необходимо вернуть значение True или False. Для примера, удалим все
# отрицательные значения из списка.
def func(elem):
    return elem >= 0
numbers = [-1, 2, -3, 4, 0, -20, 10]
positive_numbers = list(filter(func, numbers))  #  преобразуем итератор в список
print(positive_numbers)  # [2, 4, 0, 10]

# Обратите внимание: функция filter() как и функция map() возвращает не список, а специальный объект, который называется
# итератором. Итераторы можно перебрать с помощью цикла for, либо преобразовать в список.

# Встроенной функции filter() можно в качестве первого параметра func передать значение None. В таком случае каждый
# элемент последовательности будет проверен на соответствие значению True. Если элемент в логическом контексте
# возвращает значение False, то он не будет добавлен в возвращаемый результат.
true_values = filter(None, [1, 0, 10, '', None, [], [1, 2, 3], ()])
for value in true_values:
    print(value)  # 1 10 [1, 2, 3]

# В данном случае, значения списка: 0, '', None, [], () позиционируется как False, а значения 1, 10, [1, 2, 3] как True.


# Функция reduce()
# Для использования функции reduce() необходимо подключить специальный модуль functools. Функция reduce() имеет
# сигнатуру reduce(func, iterable, initializer=None). Если начальное значение не установлено, то в его качестве
# используется первое значение из последовательности iterable.
from functools import reduce
def func(a, b):
    return a + b
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = reduce(func, numbers, 0)   # в качестве начального значения 0
print(total)  # 55

# Обратите внимание на то, что мы могли вызвать функцию так:
total = reduce(func, numbers)   # в качестве начального значения первый элемент списка numbers

# Функция reduce() во второй версии языка Python была встроенной, но в Python 3 ее решили перенести в модуль functools.
# Функция reduce() как и функции map() и filter() может принимать любой итерируемый объект.


# Модуль operator
# Чтобы не писать каждый раз функции, определяющие такие стандартные математические операции как сумма или произведение:
def sum_func(a, b):
    return a + b
def mult_func(a, b):
    return a * b

# можно использовать уже реализованные функции из модуля operator.

# Неполный список функций из модуля operator выглядит так:
# Операция	            Синтаксис	Функция
# Addition	            a + b	    add(a, b)
# Containment Test	    obj in seq	contains(seq, obj)
# Division	            a / b	    truediv(a, b)
# Division	            a // b	    floordiv(a, b)
# Exponentiation	    a ** b	    pow(a, b)
# Modulo	            a % b	    mod(a, b)
# Multiplication	    a * b	    mul(a, b)
# Negation (Arithmetic)	-a	        neg(a)
# Subtraction	        a - b	    sub(a, b)
# Ordering	            a < b	    lt(a, b)
# Ordering	            a <= b	    le(a, b)
# Equality	            a == b	    eq(a, b)
# Difference	        a != b	    ne(a, b)
# Ordering	            a >= b	    ge(a, b)
# Ordering	            a > b	    gt(a, b)

# Рассмотрим примеры использования функций из модуля operator.
from operator import *     # импортируем все функции
print(add(10, 20))         # 30 сумма
print(floordiv(20, 3))     # 6 целочисленное деление
print(neg(9))              # -9 смена знака
print(lt(2, 3))            # True проверка на неравенство <
print(lt(10, 8))           # False проверка на неравенство <
print(eq(5, 5))            # True проверка на равенство ==
print(eq(5, 9))            # Fasle проверка на равенство ==

# Приведенный ниже код выводит:
from functools import reduce
import operator
words = ['Testing ', 'shows ', 'the ', 'presence', ', ', 'not ', 'the ', 'absence ', 'of ', 'bugs']
numbers = [1, 2, -6, -4, 3, 9, 0, -6, -1]
opposite_numbers = list(map(operator.neg, numbers))    #  смена знаков элементов списка
concat_words = reduce(operator.add, words)             #  конкатенация элементов списка
print(opposite_numbers)  # [-1, -2, 6, 4, -3, -9, 0, 6, 1]
print(concat_words)      # Testing shows the presence, not the absence of bugs

# Модуль operator реализован на языке C, поэтому функции этого модуля работают в разы быстрее, чем самописные функции в Python.


# Примечания
# Примечание 1. Итераторы – важная концепция языка Python. Нужно помнить:
#     итераторы можно обойти циклом for;
#     итератор можно преобразовать в список или кортеж, с помощью функций list() и tuple();
#     итератор можно распаковать с помощью *
numbers = [1, 10, -9, 8, 9, 345, -32, -89, 2]
map_obj = map(abs, numbers)
print(*map_obj)  # распаковываем 1 10 9 8 9 345 32 89 2

# Примечание 2. Если нам нужны строковые методы в виде функций, мы можем получить их через название типа str.
pets = ['alfred', 'tabitha', 'william', 'arla']
chars = ['x', 'y', '2', '3', 'a']
uppered_pets = list(map(str.upper, pets))
capitalized_pets = list(map(str.capitalize, pets))
only_letters = list(filter(str.isalpha, chars))
print(uppered_pets)      # ['ALFRED', 'TABITHA', 'WILLIAM', 'ARLA']
print(capitalized_pets)  # ['Alfred', 'Tabitha', 'William', 'Arla']
print(only_letters)      # ['x', 'y', 'a']

# Аналогично можно получить методы других типов данных в виде функций.

# Примечание 3. Подробнее прочитать про модуль operator можно в официальной документации.
# https://docs.python.org/3/library/operator.html

# Примечание 4. Модуль operator реализован на языке C, поэтому функции этого модуля работают в разы быстрее, чем
# самописные функции в Python.

# Примечание 5. В уроке, посвященном списочным выражениям, мы разбирали конструкции очень похожие на действие функций
# map() и filter(). Списочное выражение можно рассматривать как комбинацию фильтрации и трансформации: сначала
# выполняется фильтрация, затем — трансформирование.
