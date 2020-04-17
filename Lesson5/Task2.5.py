with open('qwe.txt') as f:
    lines = 0
    for line in f:
        words = len(line.split())
        lines += 1
        print(f'В {lines}-ой строке {words} строк')
