# Типы данных в Python
# Числовые (Numeric):
#     Целое (Integer)
#     Вещественное (Float)
#     Комплексное (Complex)
# Словарь (Dictionary)
# Логический (булевые) (Boolean)
# Множество (Set)
# Последовательность (Sequence Type):
#     Строка (String)
#     Список (List)
#     Кортеж (Tuple)


# Логический тип данных
# Логический тип данных (булев тип, Boolean) — примитивный тип данных в информатике, принимающий два возможных значения,
# иногда называемых истиной (True) и ложью (False). Присутствует в подавляющем большинстве языков программирования как
# самостоятельная сущность или реализуется через численный тип данных. В некоторых языках программирования за значение
# "истина" принимается 1, за значение "ложь" — 0.

# Название типа Boolean получило в честь английского математика и логика Джорджа Буля, среди прочего занимавшегося
# вопросами математической логики в середине XIX века.


# Логический тип данных в Python
# Логические значения True (истина) и False (ложь) представляют тип данных bool. У этого типа только два возможных
# значения и два соответствующих литерала: True и False.

# Мы активно использовали логический тип данных, когда работали с флажками:
flag = False

# или когда использовали условный оператор if-else:
a = 100
b = 17
if b > a:
    print('b больше a')
else:
    print('b не больше a')

# Результатом логического выражения b > a является булево значение, в данном примере False, так как значение в
# переменной b меньше значения в переменной a.

# Логические выражения можно использовать не только в условном операторе.
print(17 > 7)   # True
print(17 == 7)  # False
print(17 < 7)   # False


# Логические операторы в Python
# Для создания произвольно сложных логических выражений (условий) мы используем три логические операции:
#     и (and);
#     или (or);
#     не (not).

# Логические операции используют операнды со значениями True и False и возвращают результат также с логическими
# значениями. Определённые для объектов типа bool операторы (and, or, not) известны как логические операторы и имеют
# общеизвестные определения:
#     a and b даёт True, если оба операнда True, и False, если хотя бы один из них False;
#     a or b даёт False, если оба операнда False, и True, если хотя бы один из них True;
#     not a даёт True, если a имеет значение False, и False, если a имеет значение True.
a = True
b = False
print('a and b is', a and b)  # a and b is False
print('a or b is', a or b)    # a or b is True
print('not a is', not a)      # not a is False

# Запомните: приоритет оператора not выше, чем у оператора and, приоритет которого, в свою очередь, выше,
# чем у оператора or.


# Булевы значения как числа
# Логические значения в Python можно трактовать как числа. Значению True соответствует число 1, в то время как значению
# False соответствует 0. Таким образом мы можем сравнить логические значения с числами:
print(True == 1)   # True
print(False == 0)  # True

# Мы можем также применять арифметические операции к логическим значениям.
print(True + True + True - False)  # 3
print(True + (False / True))       # 1.0

# Возможность трактовать булевы выражения как числа на практике используется не так часто. Однако есть один прием,
# который может оказаться полезным. Поскольку True равно 11, а False равно 00, сложение логических значений вместе – это
# быстрый способ подсчета количества значений True. Это может пригодиться, когда требуется подсчитать количество
# элементов, удовлетворяющих условию.
numbers = [1, 2, 3, 4, 5, 8, 10, 12, 15, 17]
res = 0
for num in numbers:
    res += (num % 2 == 0)
print(res)  # 5


# Примечания
# Примечание 1. Вместо избыточного кода:
if flag == True:  # flag == False
    pass
# программисты обычно пишут код:
if flag:  # not flag
    pass

# Примечание 2. Операторы and и or ленивые:
#     при вычислении логического выражения x and y, если x == False, то результат всего выражения x and y будет False,
#       так что y не вычисляется;
#     при вычислении логического выражения x or y, если x == True, то результат всего выражения x or y будет True,
#       и y не вычисляется.

# Примечание 3. Математическая теория булевой логики определяет, что никакие другие операторы, кроме not, and и or,
# не нужны. Все остальные операторы на двух входах могут быть указаны в терминах этих трех операторов. Все операторы на
# трех или более входах могут быть указаны в терминах операторов двух входов.
# Фактически, даже наличие пары or и and избыточно. Оператор and может быть определен в терминах not и or, а оператор or
# может быть определен в терминах not и and. Однако, and и or настолько полезны, что во всех языках программирования
# есть и то, и другое.


# Функция bool()
# Для приведения других типов данных к булеву существует функция bool(), работающая по следующим соглашениям:
#     строки: пустая строка — ложь (False), непустая строка — истина (True);
#     числа: нулевое число — ложь (False), ненулевое число (в том числе и меньшее нуля) — истина (True);
#     списки: пустой список — ложь (False), непустой — истина (True).

print(bool('Beegeek'))              # True
print(bool(17))                     # True
print(bool(['apple', 'cherry']))    # True
print(bool())                       # False
print(bool(''))                     # False
print(bool(0))                      # False
print(bool([]))                     # False


# Функции, возвращающие булево значение
# Мы можем создавать функции, возвращающие булевы значения (True или False). Такая практика очень полезна.
# Напишем функцию is_even(), принимающую одно число и возвращающую значение True если переданное число четное и False в
# противном случае:
def is_even(num):
    return num % 2 == 0
print(is_even(8))   # True
print(is_even(7))   # False

# В программировании функция, которая возвращает значение True или False называется предикатом.


# Функция isinstance()
# В языке Python имеется встроенная функция isinstance() для проверки соответствия типа объекта какому-либо типу данных.
print(isinstance(3, int))           # True
print(isinstance(3.5, float))       # True
print(isinstance('Beegeek', str))   # True
print(isinstance([1, 2, 3], list))  # True
print(isinstance(True, bool))       # True
print(isinstance(3.5, int))         # False
print(isinstance('Beegeek', float)) # False


# Функция type()
# В языке Python имеется встроенная функция type(), позволяющая получить тип указанного в качестве аргумента объекта.
print(type(3))          # <class 'int'>
print(type(3.5))        # <class 'float'>
print(type('Beegeek'))  # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>
print(type(True))       # <class 'bool'>

# Функция type() часто бывает полезна при отладке программного кода, а также в реальном коде, особенно в
# объектно-ориентированном программировании с наследованием и пользовательскими строковыми представлениями, но об этом
# позже.

# Обратите внимание, что при проверке типов обычно вместо функции type() используется функцияisinstance() так как,
# она принимает во внимание иерархию типов (ООП).
