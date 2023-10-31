# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Notes:
# 1. define a function that takes in an array and target value
# 2. initialize two variables to help with binary search range (left, right)
# 3. Initialize while loop that calculates the middle index of current search range using floor division
# 4. if the number found at mid-index == target return mid
# 5. if the number found at mid-index is less than target, move the left boundary to mid + 1 and repeat loop
# 6. else, move the right boundary down one
# 7. Return value of left variable


def find_position(nums, target):
    left, right = 0, len(nums) - 1

    # print(right)
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            print("mid = ", mid)
            return mid
        elif nums[mid] < target:
            left = mid + 1
            print("mid here =", mid)
        else:
            right = mid - 1
            print("right = ", right)
    return left


print(find_position([1, 3, 5, 6, 7, 8], 5))
# print(find_position([1, 3, 5, 6], 2))
