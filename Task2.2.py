n = int(input('Введите количество элементов списка: '))
my_list = []
i = 0
number = 0
while i < n:
    my_list.append(int(input(f'Введите {i + 1}-й элемент списка: ')))
    i += 1

print(my_list)

for i in range(int(len(my_list) / 2)):
    my_list[number], my_list[number + 1] = my_list[number + 1], my_list[number]
    number += 2
print(my_list)
