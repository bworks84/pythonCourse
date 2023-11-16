# Given a binary array nums, return the maximum number of consecutive 1's in the array.


# input: nums = [1, 1, 0, 1, 1, 1]
# output = 3


# Notes:
# 1. find starting point of 1s in list
# 2. find end point of consecutive 1s
# 3. Would need to compare current element against next element, if elements match, increment
# a counter by 1
# 4. have a second counter var for other consecutive 1s to compare against first one


def count_ones(nums):
    longest_nums_count = 0
    current_nums_count = 0

    for element in nums:
        if element == 1:
            current_nums_count += 1
            longest_nums_count = max(longest_nums_count, current_nums_count)
        elif element != 1:
            current_nums_count = 0

    return longest_nums_count


print(count_ones([1, 1, 0, 1, 1, 1]))
print(count_ones([1, 0, 1, 1, 0, 1]))
