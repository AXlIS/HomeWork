text = input('Введите строку: ').split()

for i in text:
    if len(i) > 10:
        print(i[:10])
    else:
        print(i)
