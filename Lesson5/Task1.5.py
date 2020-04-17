with open('qwe.txt', 'w', encoding='UTF-8') as f:
    line = input('Введите текст: ')
    while line:
        f.writelines(line + '\n')
        line = input('Введите текст: ')
