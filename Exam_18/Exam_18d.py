with open ('words.txt', 'rt', encoding='utf-8') as file:
    content = file.readline().strip().split()

max_length = len(max(content, key=lambda x: len(x)))
print(*filter(lambda x: len(x) == max_length, content), sep='\n')
