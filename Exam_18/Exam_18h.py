functions_without_comments = []
with open(input(), 'rt', encoding='utf-8') as file:
    other_line = file.readline()
    if other_line[:3] == 'def':
        functions_without_comments.append(other_line[4:other_line.find('(')])
    for line in file:
        if line[:3] == 'def' and other_line[0] != '#':
            functions_without_comments.append(line[4:line.find('(')])
        other_line = line

if len(functions_without_comments) == 0:
    print('Best Programming Team')
else:
    for func in functions_without_comments:
        print(func)
