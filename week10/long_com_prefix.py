# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Notes:
# 1. Define a function that takes in a list of strings
# 2. Loop through first word, take first element and print value
# 3. Set first element value to current value and search if it matches other strings in list
# 4. If match, place current element into new variable to store longest substring
# 5. Continue to 2nd element in first string and repeat
# 6. If element does not match all strings, return variable longest substring
# 7. If no common prefix return empty string

def longest_common_prefix(strs):
    ans = ""
    strs = sorted(strs)  # sort the list to help with complexity
    first = strs[0]
    last = strs[-1]
    # This loop iterates through the characters of the strings first and last up to the length of the shorter of the two strings. The purpose of this loop is to compare characters at corresponding positions in both strings.

    for i in range(min(len(first), len(last))):
        # print("first[i] =", first[i])
        # print("last[i] =", last[i])

        if (first[i] != last[i]):
            return ans
        ans += first[i]
    return ans


print(longest_common_prefix(["Matted", "Matt", "Matter", "Mats"]))


# def common_substring(strings):
#     # Find the shortest string in the list to ensure we aren't checking more than necessary
#     min_length = min(len(s) for s in strings)
#     print(min_length)

#     common = ""
#     # loop checks chars from the beginning of each string up to the length of the shortest string
#     # remember range is iterating from (0 - min_length -1)
#     for i in range(min_length):
#         char = strings[0][i]  # Get the first character from the first string
#         # print("char = ", char)

#         # Check if the character exists in all other strings at the same index
#         # all method returns true if bool is true for all values
#         if all(string[i] == char for string in strings):
#             # print("string[i] = ", string[i])
#             common += char
#             print("common = ", common)
#         else:
#             break  # Stop when a character doesn't match in all strings

#     return common


# string_list = ["bad", "badminton", "badder", "badmama"]

# result = common_substring(string_list)
# # print("Common substring:", result)
