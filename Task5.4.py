from functools import reduce


def my_func(x, y):
    return x * y


my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(my_func, my_list))
