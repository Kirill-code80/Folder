old = int(input('Возраст: '))
if 3 <= old and old < 6:
    print('Заяц в лабиринте')
elif 6 <= old and old < 12:
    print('Марсианин')
elif 12 <= old and old < 16:
    print('Джуманджи')
elif old <=16:
    print('Интерстеллар')
else:
    print('Матрица')
