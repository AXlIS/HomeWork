def my_func():
    sum = 0
    my_str = input('Введите числа, резделяя их пробелом: ')
    my_str = my_str.title()
    while my_str != 'Stop':
        my_list = my_str.split()
        if my_list.count('Stop') == 0:
            for number in my_list:
                number = int(number)
                sum += number
            print(f'Сумма равна: {sum}')
            my_str = input('Введите числа, резделяя их пробелом '
                           '(для остановки напишите "Stop"): ')
            my_str = my_str.title()
        else:
            my_list.pop()
            for number in my_list:
                number = int(number)
                sum += number
            print(f'Сумма равна: {sum}')
            break
    print('Работа окончена!')

