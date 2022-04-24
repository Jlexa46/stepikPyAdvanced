counter = 0
with open('grades.txt', 'rt', encoding='utf-8') as file:
    for line in file:
        student = map(lambda x: int(x) >= 65, line.split()[1:])
        counter = counter + 1 if all(student) else counter
print(counter)
