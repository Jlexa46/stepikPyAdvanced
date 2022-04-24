with open('input.txt', 'r', encoding='utf-8') as f_input, open('output.txt', 'w', encoding='utf-8') as f_output:
    for i, line in enumerate(f_input, 1):
        f_output.write(str(i) + ') ' + line)
