# Running sum of 1d array

# Given an array nums. Define a running sum of an array as runningSum[i] = sum(nums[0]...nums[i])

# Example:
# Input: nums = [3, 1, 2, 10, 1]
# Output: [3, 4, 6, 16, 17]


# Steps
# set N to length of list = 5
# create for loop that iterates from i = 1 to i = N - 1, which means it will loop through the indices of the nums list from the second element to the last element
# Inside the loop, add the value at index i - 1 to the value at index i, effectively calculating the running sum by updating each element in the nums list to be the sum of itself and the previous element
# return list

nums = [1, 2, 3, 4, 5]


def runningSum(nums):
    N = len(nums)
    for i in range(1, N):
        nums[i] += nums[i-1]
    return nums


print(runningSum(nums))
