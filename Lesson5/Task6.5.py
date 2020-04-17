# Информатика: 100 (л)  50 (пр)  20(лаб).
# Физика: 30 (л)  —  10 (лаб)
# Физкультура: —  30 (пр)  —

data = {}
with open('qwe.txt', encoding='UTF-8') as f:
    for line in f:
        amount = 0
        a = line.split()  # Поделил строку
        subj = a[0].split(':')  # Выделил предмет
        for el in a:
            try:
                amount = amount + int(el)
            except ValueError:
                pass
        data[subj[0]] = amount
print(data)
