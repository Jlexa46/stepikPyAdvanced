# Bложенные списки
# Как мы уже знаем, список представляет собой упорядоченную последовательность элементов, пронумерованных от 0.
# Элементами списка могут быть любые типы данных – числа, строки, булевы значения и т.д.
numbers = [10, 3]
constants = [3.1415, 2.71828, 1.1415]
countries = ['Russia', 'Armenia', 'Argentina']
flags = [True, False]

# Элементы списка необязательно должны иметь одинаковый тип данных. Список может содержать значения разных типов данных:
info = ['Timur', 1992, 72.5]  # строка, целое число, число с плавающей точкой

# Обычно элементы списка содержат данные одного типа и на практике редко приходится создавать списки содержащие элементы
# разных типов данных.


# Вложенные списки
# Оказывается, элементами списков могут быть другие списки и на практике такая конструкция оказывается очень полезной.
# Такие списки называются вложенными списками.

# Создание вложенного списка
# Работа с вложенными списками принципиально ничем не отличается от работы со списками, например, чисел или строк.
# Чтобы создать вложенный список, мы также перечисляем элементы через запятую в квадратных скобках:
my_list = [[0], [1, 2], [3, 4, 5]]
print(my_list)          # [[0], [1, 2], [3, 4, 5]]
print(my_list[0])       # [0]
print(my_list[1])       # [1, 2]
print(my_list[2])       # [3, 4, 5]
print(len(my_list))     # 3

# Индексация
# При работе с одномерными списками мы использовали индексацию, то есть обращение к конкретному элементу по его индексу.
# Аналогично можно индексировать и вложенные списки:
my_list = ['Python', [10, 20, 30], ['Beegeek', 'Stepik']]
print(my_list[0])   # Python
print(my_list[1])   # [10, 20, 30]
print(my_list[2])   # ['Beegeek', 'Stepik']
print(my_list[0][2])       # t - индексирование строки 'Python'
print(my_list[1][1])       # 20 - индексирование списка [10, 20, 30]
print(my_list[2][-1])      # Stepik! - индексирование списка ['Beegeek', 'Stepik!']
print(my_list[2][-1][-1])  # ! индексирование строки 'Stepik!'

# Попытка обратиться к элементу списка по несуществующему индексу:
print(my_list[3])          # IndexError: index out of range - у списка my_list индексы от 0 до 2


# Функции len(), max(), min()
# Функция len()
my_list = [[0], [1, 2], [3, 4, 5], [], [10, 20, 30]]
print(len(my_list))  # 5

# Обратите внимание, встроенная функция len() возвращает количество элементов (число 5) списка my_list, а не общее
# количество элементов во всех списках (число 9).

# Если требуется посчитать общее количество элементов во вложенном списке my_list, мы можем использовать цикл for в
# связке с функцией len():
total = 0
my_list = [[0], [1, 2], [3, 4, 5], [], [10, 20, 30]]
for li in my_list:
    total += len(li)
print(total)  # 9

# Переменная li последовательно принимает все значения элементов списка my_list, то есть является сама по себе списком,
# поэтому мы можем вызывать функцию len() с переданным аргументом li.

# Функции min() и max()
# Функции min() и max() могут работать и со списками. Если этим функциям передается несколько списков, то целиком
# возвращается один из переданных списков. При этом сравнение происходит поэлементно: сначала сравниваются первые
# элементы списков. Если они не равны, то функция min() вернет тот список, первый элемент которого меньше,
# max() – наоборот. Если первые элементы равны, то будут сравниваться вторые и т. д.
list1 = [1, 7, 12, 0, 9, 100]
list2 = [1, 7, 90]
list3 = [1, 10]
print(min(list1, list2, list3))  # [1, 7, 12, 0, 9, 100]
print(max(list1, list2, list3))  # [1, 10]

# Функции min() и max() также можно использовать при работе с вложенными списками.
list1 = [[1, 7, 12, 0, 9, 100], [1, 7, 90], [1, 10]]
list2 = [['a', 'b'], ['a'], ['d', 'p', 'q']]
print(min(list1))  # [1, 7, 12, 0, 9, 100]
print(max(list1))  # [1, 10]
print(min(list2))  # ['a']
print(max(list2))  # ['d', 'p', 'q']

# Обратите внимание – элементы вложенных списков в этой ситуации должны быть сравнимы.
my_list = [[1, 7, 12, 0, 9, 100], ['a', 'b']]
# print(min(my_list))   # TypeError: '<' not supported between instances of 'str' and 'int'
# print(max(my_list))   # TypeError: '<' not supported between instances of 'str' and 'int'


# Примечания
# Примечание 1. Независимо от вложенности списков, нам нужно помнить по возможности все списочные методы:
#     1. метод append() добавляет новый элемент в конец списка.
#     2. метод extend() расширяет один список другим списком.
#     3. метод insert() вставляет значение в список в заданной позиции.
#     4. метод index() возвращает индекс первого элемента, значение которого равняется переданному в метод значению.
#     5. метод remove() удаляет первый элемент, значение которого равняется переданному в метод значению.
#     6. метод pop() удаляет элемент по указанному индексу и возвращает его.
#     7. метод count() возвращает количество элементов в списке, значения которых равны переданному в метод значению.
#     8. метод reverse() инвертирует порядок следования значений в списке, то есть меняет его на противоположный.
#     9. метод copy() создает поверхностную копию списка.
#     10. метод clear() удаляет все элементы из списка.
#     11. оператор del позволяет удалять элементы списка по определенному индексу.

# Примечание 2. Методы строк, работающие со списками:
#     1. метод split() разбивает строку на слова, используя в качестве разделителя последовательность пробельных
#       символов, символ табуляции (\t) или символ новой строки (\n).
#     2. метод join() собирает строку из элементов списка, используя в качестве разделителя строку,
#       к которой применяется метод.

# Примечание 3. Язык Python не ограничивает нас в уровнях вложенности: элементами списка могут быть списки, их
# элементами могут быть другие списки, элементами которых в свою очередь могут быть другие списки...
