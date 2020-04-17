surname = []
with open('qwe.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        a = line.split()
        if int(a[1]) < 20000:
            surname.append(a[0])
    print(surname)
