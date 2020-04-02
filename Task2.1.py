my_list = []
n = int(input('Введите колличество элементов списка: '))
last_element = None

for i in range(1, n + 1):
    my_list.append(int(input(f'Введите {i}-й элемент списка: ')))

print(my_list)

if len(my_list) % 2 == 1:
    last_element = my_list.pop()

for number, element in enumerate(my_list):
    if number % 2 == 0:
        my_list.insert(number + 2, my_list[number])
        my_list.remove(my_list[number])

if last_element != None:
    my_list.append(last_element)

print(my_list)
