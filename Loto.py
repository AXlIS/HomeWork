import random
import copy

NUMBERS = 40
CELLS = 9
numbers_list1 = random.sample(range(1, NUMBERS + 1), 40)


def create_str():
    card_list = []
    for i in range(3):
        numbers_list = random.sample(numbers_list1, 5)
        for num in numbers_list:
            numbers_list1.remove(num)
        card_list.append(sorted(numbers_list))
    return card_list


def header_generate(name):
    separator = '-' * 9
    print(f'{separator} {name} {separator}')


def create_player_card():
    card_list = create_str()
    player_card = []
    for i in card_list:
        for j in range(4):
            i.insert(random.randint(0, CELLS + 1), ' ')
    return card_list


def create_computer_card():
    card_list = create_str()
    computer_card = []
    for i in card_list:
        for j in range(4):
            i.insert(random.randint(0, CELLS + 1), ' ')
    return card_list


def card_show(name):
    visual = copy.deepcopy(name)
    for i in visual:
        for num in range(len(i)):
            try:
                i[num] = str(i[num])
            except:
                pass
        print('  '.join(i))


def check(num, card):
    global index
    index = 0
    for line in card:
        for n, n1 in enumerate(line):
            try:
                if n1 == num:
                    line[n] = '-'
                    index += 1
            except:
                pass
    return card


def generator():
    numbers_list2 = random.sample(range(1, NUMBERS + 1), 40)
    while len(numbers_list2) != 0:
        a = random.choice(numbers_list2)
        numbers_list2.pop(numbers_list2.index(a))
        yield a


def game_round():
    player_list = ['Игрок', 'Компьютер']
    player_point = 0
    computer_point = 0
    player = create_player_card()
    computer = create_computer_card()
    barrel = generator()
    while player_point != 15 and computer_point != 15:
        barrel_num = next(barrel)
        print(f'Новый бочонок: {barrel_num}')
        header_generate('Ваша карточка')
        card_show(player)
        header_generate('Компьютер')
        card_show(computer)
        answer = input('Зачеркнуть цифру? (y/n)')
        if answer == 'y':
            check(barrel_num, player)
            if index == 0:
                print('Поражение')
                break
            player_point += 1
        else:
            check(barrel_num, player)
            if index == 1:
                print('Поражение')
                break
        check(barrel_num, computer)
        if index == 1:
            computer_point += 1
    if player_point == 15:
        print('Игрок победил!')
    if computer_point == 15:
        print('Компьютер победил!')


game_round()
