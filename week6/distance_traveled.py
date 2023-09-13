'''
Program name: distance_traveled.py

Author: Rob Works
Course: Python Essentials
Date : 9/5/2023
Assignment: Module 3 - Distance Traveled
Purpose: Calculate distance traveled from user input of speed and time

'''

# distance = speed * time

vehicle_speed = int(
    input("What is the speed of the vehicle in miles per hour?\n"))
hours_traveled = int(input("How many hours has it been traveling?\n"))

headings = ["Hours", "Distance Traveled"]

print("\n")
# print headings and separate with 5 blank spaces for formatting
print(*headings, sep="   ")
print("----------------------------")  # added for formatting and readability

# loop through list and calculate distance traveled
if vehicle_speed < 0 or hours_traveled < 0:
    print("Please enter a speed and time greater than zero")
else:
    for x in range(hours_traveled):
        # print(x)
        distance = vehicle_speed * (x + 1)
        print(x + 1, "     ", distance)


""" Notes:
1. take user input for speed and time, convert to integer
2. created variable for speed and time in list format, easy to add more column titles if desired
3. printed separator to follow example format
4. created if/else statement to check if inputs match criteria, if they do then proceeded 
    to loop through hours_traveled to calculate distance and print each hourly distance
"""
