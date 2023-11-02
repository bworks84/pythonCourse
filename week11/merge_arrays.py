# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Notes:
# 1. Create function that takes in two lists and two variables taht represent length of each list
# 2. initialize empty list and two variables set to zero
# 3. create while loop that iterates through each list (i, j < lists[1,2])
# 4. if element at nth index in first list is less than element at nth index in second list
# append that element to list, else append element from second list
# 5. Increment i or j depending on condition accepted to progress through loop


# def merge_arrays(nums1, m, nums2, n):
#     i, j = 0, 0

#     while i < len(nums1) and j < len(nums2):
#         if nums1[i] == 0:
#             nums1.pop(i)  # remove zero in list
#         elif nums2[j] == 0:
#             nums2.pop(i)  # remove zero in list
#             j += 1
#         elif nums1[i] < nums2[j]:  # advance if element is less than element in list2
#             i += 1
#         else:
#             nums1.insert(i, nums2[j])
#             i += 1
#             j += 1

#     while i < len(nums1):
#         if nums1[i] != 0:
#             i += 1

#     while j < len(nums2):
#         if nums2[j] != 0:
#             nums1.append(nums2[j])
#         j += 1
#     return nums1


# print(merge_arrays([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
# print(merge_arrays([2, 0], 1, [1], 1))

# a = starts at the last index of the nums1 list
# b = starts at the last index of the nums2 list
# write_index = starts at the last available index for writing in the merged list
# while b >= 0, if there are elements left in nums1 list and the current element in nums1 is greater
# than the current element in nums2 ->


def merge(nums1, m, nums2, n):
    print("nums1[m:] =", nums1[m:])
    print("nums2[:n] = ", nums2[:n])
    nums1[m:] = nums2[:n]
    print(nums1.sort())


# print(merge([2, 0], 1, [1], 1))
print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
