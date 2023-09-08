a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

# print(c + d + e)


my_list = [1, 2, 3]
# print(my_list[-1:-2])
# # print(my_list[my_list[-1]])
# for v in range(len(my_list)):
#     my_list.insert(1, my_list[v])
#     print(my_list)
# print(my_list)

my_list_2 = []
for v in my_list:
    my_list_2.insert(0, v)
    print(my_list_2)
print(my_list_2)

# t = [[3-i for i in range(3)] for j in range(3)]
# s = 0
# for i in range(3):
#     # print(s)
#     s += t[i][i]
# print(s)

# var = 1
# while var < 10:
#     print("#")
#     var = var << 1

# z = 10
# y = 0
# x = y < z and z > y or y > z and z < y
# print(x)

# vals = [0, 1, 2]
# vals.insert(0, 1)
# del vals[1]
# print(vals)

for i in range(1):
    print(i, "#")
else:
    print("#")
