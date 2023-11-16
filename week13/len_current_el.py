# Given an array nums of integers, return how many of them contain an even number of digits.


# input: nums = [12, 345, 2, 6, 7896]
# output: 2 (12, 7896)


def find_len_current_el(nums):
    even_digits = 0

    for element in nums:
        str_element = len(str(element))
        if str_element % 2 == 0:
            even_digits += 1
            # print(even_digits)

    return even_digits


print(find_len_current_el([12, 345, 2, 6, 7896]))
print(find_len_current_el([555, 901, 482, 1771]))
