_customer = {}
for _ in range(int(input())):
    text = input().split()
    if text[1] in _customer.get(text[0], {}).keys():
        _customer[text[0]][text[1]] += int(text[2])
    else:
        _customer.setdefault(text[0], {}).update({text[1]: int(text[2])})

for key in sorted(_customer):
    print(key+':')
    {print(item, _customer[key][item]) for item in sorted(_customer[key])}
