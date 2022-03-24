Timur, Ruslan = input(), input()
if Timur == Ruslan:
    print('ничья')
elif Timur == 'камень' and Ruslan == 'бумага':
    print('Руслан')
elif Timur == 'камень' and Ruslan == 'Спок':
    print('Руслан')
elif Timur == 'ножницы' and Ruslan == 'Спок':
    print('Руслан')
elif Timur == 'ножницы' and Ruslan == 'камень':
    print('Руслан')
elif Timur == 'бумага' and Ruslan == 'ящерица':
    print('Руслан')
elif Timur == 'бумага' and Ruslan == 'ножницы':
    print('Руслан')
elif Timur == 'ящерица' and Ruslan == 'ножницы':
    print('Руслан')
elif Timur == 'ящерица' and Ruslan == 'камень':
    print('Руслан')
elif Timur == 'Спок' and Ruslan == 'ящерица':
    print('Руслан')
elif Timur == 'Спок' and Ruslan == 'бумага':
    print('Руслан')
else:
    print('Тимур')

