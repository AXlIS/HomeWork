sec = int(input('Введите время в секудах: '))
min = 0
hour = 0
hour = sec // 3600
sec = sec - (3600 * hour)
min = sec // 60
sec = sec - (60 * min)
print(f'{hour}:{min}:{sec}')