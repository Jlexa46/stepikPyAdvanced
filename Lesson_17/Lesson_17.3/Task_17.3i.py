def read_csv(__file_name='data.csv'):
    table = []
    with open(__file_name, 'rt', encoding='utf-8') as file:
        keys = file.readline().strip().split(',')
        for line in file:
            values = line.strip().split(',')
            table.append(dict(zip(keys, values)))
    return table
