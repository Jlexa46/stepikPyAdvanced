# Пустое значение
# Во многих языках программирования (Java, C++, C#, JavaScript и т.д.) существует ключевое слово null, которое можно
# присвоить переменным. Концепция ключевого слова null заключается в том, что оно дает переменной нейтральное
# или "нулевое" поведение.

# В языке Python, слово null заменено на None, поскольку слово null звучит не очень дружелюбно, а None относится именно
# к требуемой функциональности – это ничего, и не имеет поведения.


# Литерал None
# Литерал None в Python позволяет представить null переменную, то есть переменную, которая не содержит какого-либо
# значения. По сути None – это специальная константа, означающая пустоту. Если более точно, то None – это объект
# специального типа данных NoneType
var = None
print(type(var))  # <class 'NoneType'>

# Мы можем присвоить значение None любой переменной, однако мы не можем самостоятельно создать другой NoneType объект.
# Все переменные, которым присвоено значение None ссылаются на один и тот же объект типа NoneType.
# Создание собственных экземпляров типа NoneType недопустимо. Объекты, существующие в единственном экземпляре,
# называются синглтонами.


# Проверка на None
# Для того, чтобы проверить значение переменной на None, мы используем либо оператор is, либо оператор проверки на
# равенство ==.

var = None
if var is None:   # используем оператор is
  print('None')
else:
  print('Not None')

var = None
if var == None:   # используем оператор ==
  print('None')
else:
  print('Not None')

# Для сравнения переменной с None всегда используйте оператор is. Для встроенных типов поведение is и == абсолютно
# одинаково, однако с пользовательскими типами могут возникнуть проблемы, так как в Python есть возможность
# переопределения операторов сравнения в пользовательских типах.


# Сравнение None с другими типами данных
# Сравнение None с любым объектом, отличным от None дает значение False.
print(None == None)         # True
print(None == 17)           # False
print(None == 3.14)         # False
print(None == True)         # False
print(None == [1, 2, 3])    # False
print(None == 'Beegeek')    # False

print(None == 0)        # False
print(None == False)    # False
print(None == '')       # False

# Значение None не отождествляется с значениями 0, False, ''.
# Сравнивать None с другими типами данных можно только на равенство.
# print(None > 0)       # TypeError: '>' not supported between instances of 'NoneType' and 'int' ('bool')
# print(None <= False)  # TypeError: '>' not supported between instances of 'NoneType' and 'int' ('bool')


# Примечания
# Примечание 1. Обратите внимание, что функции, не возвращающие значений, на самом деле в Python
# возвращают значение None.
def print_message() :
    print('Я - Тимур,')
    print('король матана. ')
res = print_message()  # None

# Примечание 2. Концепция null значений появилась при создании языка ALGOL W великим Чарльзом Хоаром, который позднее
# назвал собственную идею ошибкой на миллиард долларов. Подробнее можно почитать тут.
