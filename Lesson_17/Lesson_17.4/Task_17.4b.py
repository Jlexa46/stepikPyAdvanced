from random import sample

with open('random.txt', 'w', encoding='utf-8') as file:
    for num in sample(range(111, 778), 25):
        print(num, file=file)
