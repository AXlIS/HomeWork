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
    analiz['товар'].append(my_tuple[1]['товар'])
    analiz['цена'].append(my_tuple[1]['цена'])
    analiz['колличество'].append(my_tuple[1]['колличество'])
    analiz['ед'].append(my_tuple[1]['ед'])

for i in range(len(my_list)):
    print(my_list[i])

for i in analiz:
    print(i, ': ',analiz[str(i)])



