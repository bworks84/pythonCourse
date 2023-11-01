# Given two binary strings a and b, return their sum as a binary string.
# Input: a = "1010", b = "1011"
#   a == 10  b == 11 output == 21 or "10101"
# Output: "10101"


# Notes:
# 1. define a function that takes in two binary string inputs
# 2. convert each binary string into integer with base argument 2, indicating the input is in binary
# 3. convert the sum of each integer back to binary with the bin method, will result in ex. Ob...
# 4. Slice the 'Ob' part of binary string off [2:] and return result


def add_binary(a, b):
    new_a = (int(a, 2))
    new_b = (int(b, 2))
    result = bin(new_a + new_b)[2:]
    return result


# print(add_binary("11", "1"))
print(add_binary("1010", "1011"))
