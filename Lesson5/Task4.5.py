numbers = {'One': 'Один',
           'Two': 'Два',
           'Three': 'Три',
           'Four': 'Четыре'}
new_list = []
with open('qwe.txt', encoding='UTF-8') as f:
    for i in f:
        a = i.split()
        new_list.append(numbers[a[0]] + ' - ' + a[2])
with open('qwe2.txt', 'x', encoding='UTF-8') as f:
    for line in new_list:
        f.write(line + '\n')












