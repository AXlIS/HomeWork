revenue = int(input('Задайте значение выручки фирмы: '))
costs =int(input('Задайте заначение расходов фирмы: '))

if revenue > costs:
    profit = revenue - costs
    print(f'Прибыль вашей компании: {profit}')
    print('Рентабельность вашей компании: ', round(profit / revenue, 2))
    workers = int(input('Введите число работников: '))
    print('Прибыль фирмы в расчете на одного работника: ', round(profit / workers, 2))
else:
    print('Ваша компания терпит убытки')