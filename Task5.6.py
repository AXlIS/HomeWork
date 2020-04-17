class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Hundle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


pen = Pen('pen')
pencil = Pencil('pencil')
hundle = Hundle('hundle')
pen.draw()
pencil.draw()
hundle.draw()
