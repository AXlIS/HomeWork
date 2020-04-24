import numpy as np


class Matrix:

    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return str(np.array(self.lists))

    def __add__(self, other):
        for i in range(len(self.lists)):
            for j in range(len(self.lists[i])):
                self.lists[i][j] = self.lists[i][j] + other[i][j]
        print(np.array(self.lists))


a = [[1, 2, 3], [4, 5, 6]]
matrix = Matrix(a)

matrix + [[2, 3, 4], [5, 6, 7]]

matrix + a
