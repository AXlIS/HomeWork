my_list = [1, 3, 2, 3, 9, 7, 1, 6, 7]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)
