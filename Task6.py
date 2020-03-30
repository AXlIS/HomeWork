a = int(input('Введите начальную дистанцию: '))
b = int(input('Выедите желаемую дистанцию: '))
index = 1.1
days = 1

print(f'{days}-й день: {a}')

while a < b:
    days += 1
    a = a * index
    print(f'{days}-й день: ', round(a, 2))

