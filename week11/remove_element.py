# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.


# Notes:
# 1. define function that takes in array and x value, then returns copy of array
# 2. Return each element of copied array
# 3. Enumerate through array, searching for index and each element (el), if el == x (value),
# then pop/append that element to place at end of list.
# 4. Then replace element that matches x with '_' character
# 4. return list


# def remove_elements(x, nums):
#     copy_nums = nums
#     removed_nums = []
#     # print(nums)
#     for i, el in enumerate(copy_nums):
#         # print("i = ", i)
#         if el == x:
#             copy_nums.pop(i)
#             removed_nums.append(el)
#     for e in range(len(removed_nums)):
#         removed_nums[e] = '_'
#     print(removed_nums)
#     print("Updated list: ", copy_nums)

#     return copy_nums + removed_nums

# Notes:
# this function differs from the instructions on leetcode, but this is what passes
# this function removes elements that match value from array, and return the length of the new array

def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            print("Nums[k] = ", nums[k])
            nums[k] = nums[i]
            k += 1
    return k


# print(remove_elements(3, [3, 2, 2, 3]))
print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
