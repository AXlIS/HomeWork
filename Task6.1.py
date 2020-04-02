my_list = []
analiz = {'товар':[], 'цена':[], 'колличество':[], 'ед': []}

n = int(input('Введите колличество товара: '))

for i in range(1, n + 1):
    my_tuple = (i, {
       'товар': input('Введите название товара: '),
       'цена': int(input('Введите цену: ')),
       'колличество': int(input('Введите колличество: ')),
       'ед': input('Введите единицу измерения: ')})
    my_list.append(my_tuple)
    for i in analiz:
        analiz[str(i)].append(my_tuple[1][str(i)])

for i in range(len(my_list)):
    print(my_list[i])

for i in analiz:
    print(i, ': ',analiz[str(i)])



