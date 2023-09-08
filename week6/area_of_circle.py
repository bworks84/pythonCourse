import math

"""
Program name: falling_distance.py

Author: Rob Works
Course: Python Essentials
Date : 9/8/2023
Assignment: Module 4 - Area of Circle 

Purpose: Calculate area, perimeter and radius of circle give users input

"""

# ASSIGNMENT 2: Area of a Circle

# The following formula gives the distance between two points, (x1, y1) and (x2, y2) in the Cartesian plane:

# dist = sqrt(x2-x1)^2 + (y2-y1)^2)

# Given the center and a point on the circle, you can use this formula to find the radius of the circle. Write a program that prompts the user to enter the center and a point on the circle (two tuples containing an x and y value). The program should then output the circle’s radius, diameter, circumference, and area. Your program must have at least the following functions:

# calculateRadius: Receives the x-y coordinates of the center and point on the circle (as input by the user) and calculates the distance between the points. This value is returned as the radius of the circle.

# calculateArea: Receives the radius of a circle, calculates and returns the area of the circle.

# calculatePerimeter: Receives the radius of a circle, calculates and returns the perimeter of the circle.

# The output should clearly display the radius, area, and perimeter of the resulting circle.


# initialize two empty dictionaries
center_of_circle = []
point_in_circle = []

# take user input and place into dictionary for center of circle
for i in range(1):
    x1 = int(input("enter the x value coordinate of the center of the circle\n"))
    center_of_circle.append(x1)
    y1 = int(input("enter the y value coordinate of the center of the circle\n"))
    center_of_circle.append(y1)
print(
    f"You've enter {center_of_circle} as the coordinates for the center of the circle")

# take user input and place into point in circle dictionary
for j in range(1):
    x2 = int(input("enter the x value coordinate of the point in the circle\n"))
    point_in_circle.append(x2)
    y2 = int(input("enter the y value coordinate of the pint in the circle\n"))
    point_in_circle.append(y2)
print(
    f"You've enter {point_in_circle} as the coordinates for the point in the circle")


radius = []


def calculateRadius():
    r = math.sqrt((point_in_circle[0] - center_of_circle[0])
                  ** 2 + (point_in_circle[1] - center_of_circle[1])**2)
    radius.append(r)
    return r


def calculateArea():
    a = 2 * math.pi * (radius[0]**2)
    return a


def calculatePerimeter():
    p = 2 * radius[0] * math.pi
    return p


print("Radius: ", calculateRadius())
print("Area: ", calculateArea())
print("Perimeter: ", calculatePerimeter())
