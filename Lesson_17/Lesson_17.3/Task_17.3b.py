with open('data.txt', 'rt', encoding='utf-8') as file:
    print(*map(str.strip, file.readlines()[::-1]), sep='\n')
