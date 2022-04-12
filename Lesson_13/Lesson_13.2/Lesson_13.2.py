# Рациональное число
# Рациональное число – это число, которое можно представить в виде дроби (m / n), где m,n соответственно, числитель и
# знаменатель, которые имеют целочисленное значение, при этом знаменатель не равен нулю.
# Например, в дроби (5 / 6) числитель m=5, а знаменатель n=6.
# Знаменатель дроби показывает количество равных частей, а числитель дроби показывает, сколько из них взято.


# Тип данных Fraction
# Для работы с рациональными числами в Python используется тип данных Fraction. Тип данных Fraction как и Decimal
# реализован программно, поэтому он в разы медленнее встроенных числовых типов данных int и float. Тип данных Fraction
# неизменяемый. Операции над данными этого типа приводят к созданию новых объектов, при этом старые не меняются.
# Чтобы использовать возможности типа данных Fraction нужно предварительно подключить модуль fractions:
from fractions import Fraction


# Создание Fraction
# Создать Fraction число можно несколькими способами:
#     из целых чисел, передав значения числителя и знаменателя дроби,
#     из строки на основании десятичного представления;
#     из строки на основании обыкновенной дроби;
#     из числа с плавающей точкой (не рекомендуется).
from fractions import Fraction
num1 = Fraction(3, 4)     # 3 - числитель, 4 - знаменатель
num2 = Fraction('0.55')
num3 = Fraction('1/9')
print(num1, num2, num3, sep='\n')  # 3/4 11/20 1/9

# Нужно быть очень внимательным при создании Fraction чисел из чисел с плавающей точкой (float), потому что float числа
# округляются внутри до ближайшего возможного, а Fraction об этом ничего не знает, поэтому копирует содержимое float.
from fractions import Fraction
num = Fraction(0.34)
print(num)

# вместо ожидаемого вывода: 17/15
# код выводит: 6124895493223875/18014398509481984

# Не рекомендуется создавать Fraction числа из float чисел. В Fraction попадет уже неправильно округленное число.
# Создавать Fraction числа нужно из целых чисел, либо из строк!

# Обратите внимание на то, что при создании рационального числа Fraction, автоматически происходит сокращение числителя
# и знаменателя дроби.
from fractions import Fraction
num1 = Fraction(5, 10)
num2 = Fraction('75/100')
num3 = Fraction('0.25')
print(num1, num2, num3, sep='\n')  # 1/2 3/4 1/4

# Так же стоит обратить внимание на вывод дробей, являющихся целыми числами.
from fractions import Fraction
num1 = Fraction(5, 1)           # 5/1 = 5
num2 = Fraction(23, 23)         # 23/23 = 1
print(num1, num2, sep='\n')     # 5 1


# Сравнение Fraction чисел
# Fraction числа можно сравнивать между собой точно так же, как и любые другие числа. Доступны 66 основных операторов
# сравнения:
#     >: больше;
#     <: меньше;
#     >=: больше либо равно;
#     <=: меньше либо равно;
#     ==:  в точности равно;
#     !=: не равно.
from fractions import Fraction
num1 = Fraction(1, 2)        # 1/2
num2 = Fraction(15, 30)      # 15/30=1/2
num3 = Fraction(3, 5)        # 3/5
num4 = Fraction(5, 3)        # 5/3
num5 = 1
num6 = 0.8
print(num1 == num2)     # True
print(num1 != num4)     # True
print(num2 > num3)      # False
print(num4 <= num1)     # False
print(num1 < num5)      # True
print(num6 > num4)      # False

# Обратите внимание на то, что мы можем сравнивать Fraction числа и целые числа (числа с плавающей точкой) без явного
# приведения типов.


# Арифметические операции над Fraction числами
# Тип данных Fraction отлично интегрирован в язык Python. С Fraction числами работают все привычные операции: сложение,
# вычитание, умножение, деление, возведение в степень.
from fractions import Fraction
num1 = Fraction('1/10')
num2 = Fraction('2/3')
print(num1 + num2)  # 23/30
print(num1 - num2)  # -17/30
print(num1 * num2)  # 1/15
print(num1 / num2)  # 3/20

# Мы также можем совершать арифметические операции над Fraction и целыми числами (миксовать Fraction и int),
# но не рекомендуется смешивать их с float.
from fractions import Fraction
num = Fraction('3/8')
print(num + 1)   # 11/8
print(num - 1)   # -5/8
print(num * 2)   # 3/4
print(num ** 4)  # 81/4096

# Обратите внимание, на то, что операция возведения в степень (**) для Fraction чисел может возвращать вещественный
# результат.
from fractions import Fraction
num1 = Fraction('3/8')
num2 = Fraction('1/2')
print(num1 ** num2)  # 0.6123724356957945

# По сути тут происходит вычисление числа (3 / 8) ** (1 / 2) = math.sqrt(3 / 8) ≈ 0.6123724356957945


# Математические функции
# Fraction числа можно передавать как аргументы функций, ожидающих float. Тогда они будут преобразованы во float.
# К примеру, модуль math оперирующий float числами, может работать и с Fraction числами.
from fractions import Fraction
from math import *
num1 = Fraction('1.44')
num2 = Fraction('0.523')
print(sqrt(num1))        # 1.2
print(sin(num2))         # 0.4994813555186418
print(log(num1 + num2))  # 0.6744739152943241

# Важно понимать, что результатом работы функций модуля math являются float числа, а не Fraction.


# Свойства numerator и denominator
# Для получения числителя и знаменателя Fraction числа используются свойства numerator и denominator.
from fractions import Fraction
num = Fraction('5/16')
print('Числитель дроби равен:', num.numerator)      # Числитель дроби равен: 5
print('Знаменатель дроби равен:', num.denominator)  # Знаменатель дроби равен: 16

# В Python 3.8 появился метод as_integer_ratio(), который возвращает кортеж, состоящий из числителя и знаменателя
# данного Fraction числа.
from fractions import Fraction
num = Fraction('-5/16')
print(num.as_integer_ratio())  # (-5, 16)


# Метод limit_denominator()
# Метод limit_denominator() возвращает самую близкую к данному числу рациональную дробь, чей знаменатель не превосходит
# переданного аргумента.
from fractions import Fraction
import math
print('PI =', math.pi)
num = Fraction(str(math.pi))
print('No limit =', num)
for d in [1, 5,  50, 90, 100, 500, 1000000]:
    limited = num.limit_denominator(d)
    print(limited)

# Метод limit_denominator() позволяет получить очень точные рациональные приближения иррациональных чисел, что очень
# удобно во многих математических задачах.


# Примечания
# Примечание 1. Для того, чтобы каждый раз не писать название типа, можно использовать следующий код:
from fractions import Fraction as F
num1 = F('1/5') + F('3/2')
num2 = F('1/4') * F('2/5')
print(num1)
print(num2)

# Примечание 2. Полное руководство по данному типу данных находится в официальной документации.
# https://docs.python.org/3/library/fractions.html

# Примечание 3. В Python нельзя совершать арифметические операции (+, -, *, /) между типами Decimal и Fraction.
from decimal import Decimal
from fractions import Fraction
num1 = Decimal('12.5')
num2 = Fraction(19, 3)
# print(num1 + num2)  # TypeError: unsupported operand type(s) for +: 'Decimal' and 'Fraction'

