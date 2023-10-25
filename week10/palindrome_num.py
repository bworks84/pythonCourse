# Given an integer x, return true if x is a palindrome and false otherwise

# Notes:
# 1. define function that returns parameter
# 2. put integer into string to use splicing method
# 3. print x as is
# 4. print x using splicing method that reverses input
# - [::-1] - no start index, no stop index, step of -1, index defaults to 0, so first element is 0 - 1, second element -1 - 1, and so on...putting string in reverse
# 4. Check if reverse string = string


num = str(12271)


def palindrome_check(x):
    print(x[::])
    print("x = ", x)
    print("x reversed = ", x[::-1])
    return x == x[::-1]


print(palindrome_check(num))
