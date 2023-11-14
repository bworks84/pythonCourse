def square_root_loop():
    my_list = []
    i = 10

    while i >= 0:
        square = (i + 1) * (i + 1)
        my_list.append(square)
        i -= 1

    return my_list


print(square_root_loop())


def another_loop():
    my_list = []
    i = 0

    while i <= 10:
        square = (i + 1) * (i + 1)
        my_list.append(square)
        i += 1

    return my_list


print(another_loop())


# for each loop of the same function
my_list = [0, 1, 2, 3, 4, 5]

for element in my_list:
    square = element * element
    print(square)
