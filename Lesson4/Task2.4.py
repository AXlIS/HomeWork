my_list = [1, 5, 6, 3, 9, 2]

new_list = [el for i, el in enumerate(my_list) if my_list[i - 1] < my_list[i]]
print(new_list)