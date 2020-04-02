n = int(input('Ведите колличество чисел: '))
my_list = []
for i in range(1, n + 1):
    my_list.append(int(input(f'Ведите {i}-е число:')))
    my_list.sort(reverse= True)

print(my_list)