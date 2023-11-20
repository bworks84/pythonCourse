# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.


# arr = [1, 0, 2, 3, 0, 4, 5, 0]
# output = [1, 0, 0, 2, 3, 0, 0, 4]


# Notes
# 1. def function that takes an array and prints each element
# 2. create new empty list, loop through array and check if equal to zero
# 3. if equal to zero, make i + 1 = element, and continue iterating through loop


def duplicate_zeros(nums):
    new_list = []
    orig_len = len(nums)
    for element in nums:
        new_list.append(element)
        if element == 0:
            new_list.append(0)

    new_list = new_list[:orig_len]
    nums = new_list
    print(nums)


# print(duplicate_zeros([1, 0, 2]))  # --> [1, 0, 0]
# print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))


# Notes:
# First way was not modifying list in place
# This function, captures original length of arr and initializes an index variable with value of zero
# Loops index (starting at zero) is less than length of input array
# if element == 0, insert a zero, and increment index by 2 to skip over added zero
# else just increment loop by one
# lastly, cut array length to original length

def another_way(arr):
    orig_len = len(arr)
    index = 0

    while index < orig_len:
        if arr[index] == 0:
            print(arr[index])
            arr.insert(index, 0)
            index += 2
        else:
            index += 1

    arr[:] = arr[:orig_len]
    print(arr)


print(another_way([1, 0, 2, 3, 0, 4, 5, 0]))
