# Добавление элементов
# Мы научились создавать множества, элементы которых известны на этапе создания. Следующий шаг – научиться добавлять
# элементы в уже существующие множества.

# Метод add()
# Для добавления нового элемента в множество используется метод add().
numbers = {1, 1, 2, 3, 5, 8, 3}  # создаем множество
numbers.add(21)  # добавляем число 21 в множество
numbers.add(34)  # добавляем число 34 в множество
print(numbers)   # {1, 2, 3, 34, 5, 8, 21}

# Не забывайте, что порядок элементов при выводе множества абсолютно произвольный.

# Обратите внимание, для использования метода add() требуется предварительно созданное множество, при этом оно может
# быть пустым.
numbers = set()  # создаем пустое множество
numbers.add(1)
numbers.add(2)
numbers.add(3)
numbers.add(1)
print(numbers)  # {1, 2, 3}

# Если требуется внести несколько значений в множество, то можно воспользоваться циклом for.
numbers = set()  # создаем пустое множество
for i in range(10):
    numbers.add(i*i + 1)
print(numbers)  # {1, 2, 65, 5, 37, 10, 17, 50, 82, 26}


# Удаление элемента
# Для удаления элементов из множества используются методы:
#     remove();
#     discard();
#     pop().

# Метод remove()
# Метод remove() — удаляет элемент из множества с генерацией исключения (ошибки) в случае, если такого элемента нет.
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print(numbers)      # {1, 2, 4, 5}

# numbers = {1, 2, 3, 4, 5}
# numbers.remove(10)  # приводит к возникновению ошибки KeyError
# print(numbers)

# Метод discard()
# Метод discard() — удаляет элемент из множества без генерации исключения (ошибки), если элемент отсутствует.
numbers = {1, 2, 3, 4, 5}
numbers.discard(3)
print(numbers)      # {1, 2, 4, 5}

# Метод pop()
# Метод pop() — удаляет и возвращает случайный элемент из множества с генерацией исключения (ошибки) при попытке
# удаления из пустого множества.
numbers = {1, 2, 3, 4, 5}
print('до удаления:', numbers)      # до удаления: {1, 2, 3, 4, 5}
num = numbers.pop()                 # удаляет случайный элемент множества, возвращая его
print('удалённый элемент:', num)    # удалённый элемент: 1
print('после удаления:', numbers)   # после удаления: {2, 3, 4, 5}

# Метод pop() можно воспринимать как неконтролируемый способ удаления элементов по одному из множества.

# Метод clear()
# Метод clear() удаляет все элементы из множества.
numbers = {1, 2, 3, 4, 5}
numbers.clear()
print(numbers)   # set()

# Обратите внимание на то, что пустое множество выводится как set(), а не как {}. С помощью {} выводится пустой словарь.

# Примечания
# Примечание 1. Если мы не изменяли множество, порядок обхода элементов при помощи цикла for не изменится.

# Примечание 2. После изменения множества (методы add(), remove(), и т.д.) порядок элементов может измениться
# произвольным образом.
