filename = input()

with open(filename, 'rt', encoding='utf-8') as file:
    print(len(file.readlines()))
