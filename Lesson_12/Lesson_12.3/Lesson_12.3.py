# Метод Монте-Карло
# Метод Монте-Карло – группа численных методов, основанных на воспроизведении и статистическом анализе большого числа
# реализаций случайного процесса. Проводится математическое моделирование случайных процессов и параметры их реализации
# оцениваются статистически. Метод лежит в основе статистического моделирования.

# Метод Монте-Карло часто называют методом статистических испытаний.

# Статистическое моделирование широко применяется для решения задач из различных областей человеческого знания -
# биологии, химии, физики, экономики и других. Задачи, где широко используется этот подход:
#     численное интегрирование;
#     расчеты в системах массового обслуживания;
#     расчеты качества и надежности изделий;
#     расчеты прохождения нейтронов и других частиц через вещество;
#     передача сообщений при наличии помех;
#     задачи теории игр;
#     задачи динамики разреженного газа;
#     задачи дискретной оптимизации;
#     задачи финансовой математики.


# Вычисление площадей
# Применим метод Монте-Карло и к задаче вычисления площади геометрической фигуры на плоскости.
# Поместим фигуру в прямоугольник и будем наугад бросать точки в этот прямоугольник. Будем исходить из того, что чем
# больше площадь фигуры, тем чаще в нее будут попадать точки. Таким образом, при большом числе n точек, наугад выбранных
# внутри прямоугольника, доля точек, содержащихся в данной фигуре k, приближенно равна отношению площади этой фигуры и
# площади прямоугольника.

# Если площадь прямоугольника равна S_0 и в результате испытаний, из которых при k исходах случайные точки оказались
# внутри фигуры, то площадь S фигуры будет определяться выражением:
# S = (k / n) * S_0

# Рассмотрим алгоритм решения задачи на конкретных примерах.
# Пример 1. Рассмотрим фигуру, множество точек которой определяется следующей системой неравенств:
# (0 <= x <= 1) and (0 <= y <= 1) and (y <= x**2)

# Площадь такой фигуры S = 1 / 3 ≈ 0.33333 (считается через интеграл).

# Алгоритм Монте-Карло: площадь искомой фигуры составляет часть квадрата со сторонами 1. Площадь такого квадрата равна 1
#    1. Генерируем случайные числа x и y равномерно распределенные на отрезке [0;1]. Это будут координаты случайной
#       точки в квадрате, в которую заключена фигура, площадь которой требуется найти. Полученная точка может как
#       попасть в исследуемую фигуру, так и не попасть.
#    2. Проверяем принадлежность точки к исследуемой фигуре. Если попадания нет, т.е. не выполняется неравенство y≤x**2,
#       то переходим к пункту 1 и генерируем координаты новой точки. Если попадание есть, то фиксируем это попадание,
#       то есть увеличиваем на единицу значение счетчика числа попаданий и снова переходим к пункту 1.

# Примечание. Заметим, что попадание случайной точки точно на границу фигуры можно отнести как к первому, так и ко
# второму исходу.

# Пункты 1 и 2 следует повторить в цикле достаточно большое количество n раз. От количества повторений напрямую зависит
# точность результата. После проведения n повторов площадь фигуры найдем по формуле:
# S = (k / n) * S_0

# Пример программы на Python:
import random
n = 1000
k = 0
s0 = 1
for _ in range(n):
    x = random.uniform(0, 1)     # случайное число с плавающей точкой от 0 до 1
    y = random.uniform(0, 1)     # случайное число с плавающей точкой от 0 до 1
    if y <= x**2:                # если попадает в нужную область
        k += 1
print((k/n)*s0)

# Составим таблицу:
# n	            S
# 10	        0.6
# 100	        0.37
# 1000	        0.337
# 10000	        0.3337
# 100000  	    0.33329
# 1000000 	    0.333571
# 10000000    	0.3332828
# 100000000   	0.33336707

# Пример 2. Рассмотрим фигуру, множество точек которой определяется следующей системой неравенств:
# (-2 <= x <= 2) and (-2 <= y <= 2) and (y**3 - 2*x**2 <= -1) and (2*y + x**3 <= 3)

# Площадь этой фигуры нам заранее известна и равна S=8.38404

# Алгоритм Монте-Карло: площадь искомой фигуры составляет часть квадрата со сторонами 4.
# Площадь такого квадрата равна 16.
#     1. Генерируем случайные числа x и y, равномерно распределенные на отрезках [−2;2]. Это будут координаты случайных
#        точек в квадрате, в который заключена фигура искомой площади. Полученная точка может как попасть в исследуемую
#        фигуру, так и не не попасть.
#     2. Проверяем принадлежность точки к исследуемой фигуре. Если попадания нет, не выполняется хотя бы одно из
#        неравенств y**3 - 2*x**2 <= -1 или 2*y + x**3 <= 3, переходим к пункту 1 и генерируем координаты новой точки.
#        Если попадание есть, фиксируем это попадание, то есть увеличиваем на единицу значение счетчика числа попаданий
#        и снова переходим к пункту 1.
import random
n = 1000
k = 0
s0 = 16
for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    if y**3 - 2*x**2 <= -1 and 2*y + x**3 <= 3:
        k += 1
print((k/n)*s0)

# Составим таблицу:
# n	        S
# 10	    9.6
# 100	    8.96
# 1000    	8.224
# 10000   	8.3824
# 100000  	8.36528
# 1000000 	8.383376
# 10000000	8.3841584
# 100000000 8.38404134


# Примечания
# Примечание 1. Свое экзотическое название метод получил от города Монте-Карло в княжестве Монако, известного благодаря
# казино, поскольку именно рулетка является одним из самых широко известных генераторов случайных чисел. Станислав Улам
# пишет в своей автобиографии «Приключения математика», что название было предложено Николасом Метрополисом в честь его
# дяди, азартного игрока.

# Примечание 2. Активное применение метода началось с появлением ЭВМ, способных выполнять сотни операций для получения
# необходимых статистических данных. Развитие метода Монте-Карло пришлось на 1950-е годы, когда его использовали ученые
# из лаборатории ВВС США и исследовательской корпорации RAND, работающие над созданием водородной бомбы, в том числе и
# гениальный ученый Джон фон Нейман. Неймана считают одним из основателей метода, как, впрочем, и самих ЭВМ.

# Примечание 3. Аналогичным образом можно вычислять объемы тел в пространстве.

# Примечание 4. Подробнее о методе Монте-Карло можно почитать тут.
# https://ru.abcdef.wiki/wiki/Monte_Carlo_method


# Болотная сортировка
# Болотная сортировка (Bogosort) — неэффективный алгоритм сортировки, используемый только в образовательных целях и
# противопоставляемый другим, более реалистичным алгоритмам.

# Принцип работы алгоритма прост, как плесень. Перетряхиваем список случайным образом до тех пор пока он внезапно не
# отсортируется. Процесс может счастливо завершиться сразу, а может длиться до тепловой смерти Вселенной. Это уж как
# повезёт.

# Bogo sort is the fastest sort if you're very lucky.


# Время работы алгоритма
# Среднее время работы алгоритма болотной сортировки на современном компьютере:
# Кол-во элементов	10	     11	     12	    13	    14	    15	     16	    17       18      19	     20
# Среднее время	    0,0037 с 0,045 с 0,59 с 8,4 с	2,1 мин 33,6 мин 9,7 ч  7,29 сут 139 сут 7,6 лет 160 лет

# Колода в 32 карты будет сортироваться компьютером в среднем 2,7 * 10**19 лет.


# Реализация алгоритма
# Для реализации алгоритма болотной сортировки будем использовать функцию shuffle(), которая случайным образом перемешивает содержимое списка.
import random

def is_sort(nums):                   # отсортирован ли список?
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

def bogosort(nums):                  # реализация алгоритма болотной сортировки
    while not is_sort(nums):
        random.shuffle(nums)
    return nums

numbers = list(range(10))
random.shuffle(numbers)              # перемешиваем начальный список
print(numbers)                       # выводим начальный список

sorted_numbers = bogosort(numbers)

print(sorted_numbers)                # выводим отсортированный список
