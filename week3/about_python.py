# import math
# import time

# A = 40
# offset = 40

# for y in range(1):
#     for x in range(0, 359, 15):
#         radians = 2 * math.pi * x / 360
#         index1 = int(offset + (A * math.sin(radians)))
#         # calculate a second index by adding PI to the angle_in_radians
#         index2 = int(offset + (A * math.sin(radians + math.pi)))
#         line = ""
#         for j in range(A * 2 + 1):
#             if j == index1 or j == index2:  # add OR comparison for the second index
#                 line = line + "*"
#             else:
#                 line = line + " "
#         print(line)
#         time.sleep(0.1)


def about_python():
    print("The creator of Python is Guido van Rossum")
    print("Python was first released on February 20, 1991")
    print("The acronym BDFL stands for Benevolent dictator for life, a title given to a small number of open-source software development leaders, who retain the final say in disputes within the community")


about_python()

# print("Hello World!")

# my_text = "Hello World!"
# print(my_text)

# print("Football", 3, [1, 5], {"name": "Rob"})
