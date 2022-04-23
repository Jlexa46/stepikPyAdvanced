with open('population.txt', 'rt', encoding='utf-8') as population:
    for country in population:
        key, value = country.split('\t')[0].strip(), int(country.split('\t')[1].strip())
        if key[0] == 'G' and value > 500000:
            print(key)
