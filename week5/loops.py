for i in range(1, 11):
    if i % 2:
        print(i)

x = 1
while x < 11:
    if x % 2:
        print(x)
    x += 1

################################

email = "john.smith@pythoninstitute.org"

for ch in email:
    if ch == "@":
        new_string = email[:email.index("@")]
print(new_string)

#################################

tel_num = "0610893093"

for digit in tel_num:
    if digit == "0":
        new_string += "X"
    else:
        new_string += digit
print(new_string)


##################################

# Example 1
# word = "Python"
# for letter in word:
#     print(letter, end="*")

# Example 2
# for i in range(1, 10):
#     if i % 2 == 0:
#         print(i)

# text = "OpenEDG Python Institute"
# for letter in text:
#     if letter == "P":
#         break
#     print(letter, end="")

# n = 0

# while n != 3:
#     print(n)
#     n += 1
# else:
#     print(n, "else")

# print()

# for i in range(0, 3):
#     print(i)
# else:
#     print(i, "else")

# for i in range(3):
#     print(i, end=" ")  # Outputs: 0 1 2

# for i in range(6, 1, -2):
#     print(i, end=" ")  # Outputs: 6, 4, 2
