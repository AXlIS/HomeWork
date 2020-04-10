from itertools import count, cycle

for el in count(int(input('Введите стартовое число '))):
    print(el)

my_list = ['qwe', 123, True]
for el in cycle(my_list):
    print(el)