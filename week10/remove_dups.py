# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.


# NOTES:
# Define a function that returns a list
# Loop through the list and compare i to i + 1
# if they do not match, keep i in new list and increment a variable by one
# return list and variable count


# def removeDuplicates(nums):
#     nums = sorted(nums)
#     new_list = []
#     duplicates = []
#     k = 0

#     for item in nums:
#         if item not in new_list:
#             new_list.append(item)
#             k += 1
#             print("K = ", k)
#         elif item in new_list:
#             duplicates.append(item)
#     # output = f"{k}, new_list = {new_list}"
#     print(output)
#     return output


# print(removeDuplicates([1, 1, 2, 3, 3, 3, 4, 4, 5]))
# print(removeDuplicates([1, 1, 2]))

def removeDuplicates(nums):
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            print("nums[j] = ", nums[j])
            j += 1

    return j


print(removeDuplicates([1, 1, 2]))
