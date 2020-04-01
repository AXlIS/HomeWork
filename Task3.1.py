my_list = ['Зима', 'Весна', 'Лето', 'Осень']
my_dict ={1:'Зима', 2:'Весна', 3:'Лето', 4:'Осень'}

month = int(input('Введите номер месяца: '))

if month == 12 or month == 1 or month == 2:
    print(my_list[0])
    print(my_dict[1])
elif month == 3 or month == 4 or month == 5:
    print(my_list[1])
    print(my_dict[2])
elif month == 6 or month == 7 or month == 8:
    print(my_list[2])
    print(my_dict[3])
else:
    print(my_list[3])
    print(my_dict[4])