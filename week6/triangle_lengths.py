'''
Program name: triangle_lengths.py

Author: Rob Works
Course: Python Essentials
Date : 9/5/2023
Assignment: Module 3 - Triangle Lengths
Purpose: Determine different types of triangles based on user inputs 

'''

distances = list(
    map(int, input("Please enter three lengths above zero for a triangle. ").split()))
print("Distances: ", distances)

# sort to make first calculation of 'if triangle' more simple
x, y, z = sorted(distances)


# print(x)
# print(y)
# print(z)

# check if all inputs are above zero
def not_zero_length(x, y, z):
    if x <= 0:
        print("Please re-enter lengths above the number zero")
    elif y <= 0:
        print("Please re-enter lengths above the number zero")
    elif z <= 0:
        print("Please re-enter lengths above the number zero")
    else:
        return True


not_zero_length(x, y, z)

if x + y <= z:
    print("Those lengths do not make a triangle. A triangle has three sides where the sum of the length of any two of the sides must exceed the other side.")
else:
    if z**2 == (x**2) + (y**2):
        print("Those lengths make a right triangle!")  # ex 12 35 37
    elif x == y and x == z:
        print("Those lengths make an isosceles triangle!")  # ex 3 3 6
    elif x == y or y == z or x == z:
        print("Those lengths make an equilateral triangle!")  # 4 4 4
    else:
        print("That might be a scalene or obtuse triangle....")


"""
Notes:
1. take user input, put into list, map over the elements and split with comma
2. create 3 variables and sort for simpler comparisons
3. check if any lengths are less than zero, call function
4. evaluate lengths to determine if they make a triangle first, then evaluate if they make one of the three triangles
    listed for the assignment. 
5. scalene and obtuse triangles are not evaluated, so make exception of lengths fit first criteria but not the 
    three triangle calculations

"""
