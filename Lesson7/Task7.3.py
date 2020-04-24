class Cell:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return str(f'Колличество клеток: {self.amount}')

    def __add__(self, other):
        return self.amount + other.amount

    def __sub__(self, other):
        if self.amount - other.amount < 0:
            print('Разность количества ячеек двух клеток меньше нуля')
        else:
            print(self.amount - other.amount)

    def __mul__(self, other):
        return self.amount * other.amount

    def __truediv__(self, other):
        return self.amount / other.amount

    def make_order(self):
        pass


cell = Cell(12)
cell2 = Cell(500)
print(cell)
print(cell + cell2)
cell - cell2
print(cell.__mul__(cell2))
print(cell.__truediv__(cell2))
