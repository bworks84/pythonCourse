
"""
Program name: falling_distance.py

Author: Rob Works
Course: Python Essentials
Date : 9/8/2023
Assignment: Module 4 - Falling Distance
Purpose: Calculate falling distance based on gravity and time calculation, weight is constant


    ASSIGNMENT 1: Falling Distance

When an object is falling because of gravity, the following formula can be used to determine the distance the object falls in a specific time period:

d = 1/2 gt2

The variables in the formula are as follows: d is the distance in meters, g is 9.8, and t is the amount of time, in seconds, that the object has been falling.

Write a function named fallingDistance that accepts an object’s falling time (in seconds) as an argument. The function should return the distance, in meters, that the object has fallen during that time interval. Write a program that demonstrates the function by prompting the user for the total time and calling the function in a loop that passes the time values in 5 second increments as the argument and displays the elapsed time and return value. The output should have a header identifying the column names and tabular formatted values (values displayed are to illustrate formatting only):

Time	Distance
0	0.0
5	30.0
10	45.0
15	52.0

"""
g = 9.8

time_Seconds = int(input("Enter a time in seconds\n"))

# distance_traveled = 1/2 * gravity rate * (input time in seconds squared)


def fallingDistance(time_Seconds):
    distance_traveled = 0.5 * g * (time_Seconds ** 2)
    return distance_traveled


distance_traveled = int(time_Seconds / 2)

print("Secs\tDistance")
# used d to give better range of time/distance than just 5
for i in range(d):
    # calculates time in increments of 5 (seconds) -> 0 + 1 = 1 * 5
    time = (i + 1) * 5
    # formatting the print statement, rounding the calc of func by 2 places
    print(str(time) + "\t" + str(round(fallingDistance(time), 2)))
