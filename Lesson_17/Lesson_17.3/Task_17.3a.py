with open('text.txt', 'rt', encoding='utf-8') as file:
    print(file.readline().strip()[::-1])
