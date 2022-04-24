with open('class_scores.txt', 'rt', encoding='utf-8') as fi, open('new_scores.txt', 'wt', encoding='utf-8') as fo:
    for line in fi:
        fo.write(line.strip().split()[0] + ' ' + str(100 if int(line.strip().split()[1]) > 94 else int(line.strip().split()[1]) + 5) + '\n')
