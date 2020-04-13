def division(x, y):
    """
    Функция для деления
    x - делимое
    y - делитель
    """
    try:
        result = x / y
        print(round(result, 2))
    except ZeroDivisionError:
        print('Деление на ноль!')
    except TypeError:
        print('Пишите только цифры')



division(57637, 68)
