# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# input = [-4, -1, 0, 3, 10]
# output = [0, 1, 9, 16, 100]


# Notes:
# 1. def function that takes an array and prints each element of the array
# 2. take each element and multiply by itself, then print value
# 3. put each squared element into a new empty list
# 4. return new list sorted


def square_array(nums):
    new_list = []
    for element in nums:
        square = element * element
        new_list.append(square)

    new_list.sort()
    return new_list


print(square_array([-4, -1, 0, 3, 10]))
