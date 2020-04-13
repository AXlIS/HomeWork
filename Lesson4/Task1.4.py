import sys


def salary():
    production = int(input('Введите размер выработки в час: '))
    rate = int(input('Введите размер часовой ставки: '))
    prize = int(input('Введите размер премии: '))
    result = (production * rate) + prize
    print(result)


command = sys.argv[1]

if command == 'salary':
    salary()
