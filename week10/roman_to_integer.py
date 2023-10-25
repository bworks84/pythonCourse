# Given a roman numeral, convert it to an integer.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000


def roman_to_integer(s):
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0
    prev_value = 0

    for index, numeral in enumerate(s):
        current_value = roman_dict[numeral]
        # print("Index = ", index)
        # print("Roman numeral = ", numeral)
        # print("Previous value = ", prev_value)
        # print("Current Value = ", current_value)
        if index > 0 and current_value > prev_value:
            result += current_value - 2 * prev_value
            # print("Result = ", result)
        else:
            result += current_value
        prev_value = current_value
        # print("Total += current value = ", result)
    return result


# print(roman_to_integer("LX"))  # 60
# print(roman_to_integer("MLX"))  # 1060
# print(roman_to_integer("MMXXIII"))  # 2023
print(roman_to_integer("MCMXCVIII"))


# Notes:
# 1. Define function that takes in a roman numeral
# 2. Define a dictionary that key/value pairs are roman numerals/integers
# 3. Define two variables that will hold result and previous_value for calculations
# 4. Using enumerate in a for loop, iterate through the roman numeral,
# 5. Set current_value as the current roman numeral at each index
# 6. If index is not first element and current value is greater than previous value (to account for roman numeral crazy subtraction rule), result will equal result + current value - previous value * 2.
# Note -> this makes more sense when using print, it essentially calculates the previous value * 2 and removes that from current value, then add that value to result
# 7. If first condition is not applicable, result = result + current value, just simple addition
# 8. Lastly make previous value set to current value before beginning loop again
# 9. Return result, and a half dozen print statements
