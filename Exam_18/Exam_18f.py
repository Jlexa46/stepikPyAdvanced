with open('forbidden_words.txt', 'rt', encoding='utf-8') as file:
    forbidden = file.readline().strip().split()
    forbidden_words = {}
    for word in forbidden:
        forbidden_words[word] = '*' * len(word)

with open(input(), 'rt', encoding='utf-8') as file:
    for line in file:
        row = line.strip()
        row_lower = row.lower()
        for key, value in forbidden_words.items():
            row_lower = row_lower.replace(key, value)
        for i in range(len(row)):
            print(row_lower[i] if row_lower[i] == '*' else row[i], end='')
        print()
