import os
my_list = []
with open('qwe3.txt', 'w', encoding='UTF-8') as f:
    f.write(input('Введите числа через пробел: '))
with open('qwe3.txt', encoding='UTF-8') as f:
    a = f.read()
    for i in a.split():
        my_list.append(int(i))
print(sum(my_list))
os.remove('qwe3.txt')

