def pretty_print(data, side='-', delimiter='|'):
    line = f'{delimiter} '+ f' {delimiter} '.join([str(el) for el in data]) + f' {delimiter}'
    border = ' ' + side * (len(line)-2)
    print(border + '\n' + line + '\n' + border)
