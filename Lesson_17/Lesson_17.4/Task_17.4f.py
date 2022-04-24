files = []
for _ in range(int(input())):
    files.append(input().strip())

for file in files:
    f_input = open(file, 'rt', encoding='utf-8')
    f_output = open('output.txt', 'a', encoding='utf-8')
    for line in f_input:
        f_output.write(line)
    f_input.close()
    f_output.close()
