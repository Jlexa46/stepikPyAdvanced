from random import sample

with open('first_names.txt', 'rt', encoding='utf-8') as first_name, \
        open('last_names.txt', 'rt', encoding='utf-8') as last_name:
    firstname = list(map(str.strip, first_name.readlines()))
    lastname = list(map(str.strip, last_name.readlines()))

for _ in range(3):
    print(*sample(firstname, 1), *sample(lastname, 1))
