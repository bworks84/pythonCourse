# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.


# Notes
# 1. define a function that takes a string, create variable that holds value of string after removing any whitespace first
# 2. Loop through string split the string


def last_word(str):
    sanitized_str = str.strip().split()
    # print(sanitized_str)
    # res = sanitized_str.split()
    len_last_word = len(sanitized_str[-1])
    last_word_s = sanitized_str[-1]
    print(f"The last word is '{last_word_s}' with a length of {len_last_word}")
    # print(len_last_word)
    # print(last_word_s)


print(last_word(" Hello World "))
