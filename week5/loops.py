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

vals = [0, 1, 2]
vals.insert(0, 1)
print(vals)
del vals[1]

print(vals)

z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)

i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print("*")

my_list = [3, 1, -2]
print(my_list[my_list[-1]])

t = [[3-i for i in range(3)] for j in range(3)]
s = 0
for i in range(3):
    s += t[i][i]
    print(s)
print(s)

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
