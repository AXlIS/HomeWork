def my_func(x, y, z):
    my_list = [x, y, z]
    list_max = []
    max_1 = max(my_list)
    my_list.remove(max_1)
    list_max.append(max_1)
    max_2 = max(my_list)
    list_max.append(max_2)
    print(sum(list_max))


my_func(4, 78, 24)

