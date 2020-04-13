def my_func1(x, y):
    return x ** abs(y)


def my_func2(x, y):
    index = x
    for i in range(abs(y - 1)):
        x = x * index
    return x


print(my_func1(2, 5))
print(my_func2(2, 5))
