"""
Rob Works
Python Essentials
8/23/23

Module 2 Assignment #2

Weight on Other Planets:

You can calculate an individual's weight on another planet by multiplying their weight times the relative surface gravity of the other world.

Weight on Other Planet = Weight on Earth x Multiple of Earth’s Gravity

Design a Python program that asks a user for their name and weight. The program will greet the user by name and then calculate/display the user's weight on the other planets. Each item should be displayed on a line by itself.

Use the following values for the conversions

Body Multiple of Earth’s Gravity
Sun 27.01
Mercury 0.38
Venus 0.91
Earth 1 (defined)
Moon 0.166
Mars 0.38
Jupiter 2.34
Saturn 1.06
Uranus 0.92
Neptune 1.19
Pluto 0.06
    
"""

planets = {
    "Sun": 27.01,
    "Mercury": .38,
    "Venus": .91,
    "Earth": 1,
    "Moon": .166,
    "Mars": .38,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus": .92,
    "Neptune": 1.19,
    "Pluto": .06
}

first_name = input("Hello, what is your first name?\n")
weight = input("What is your weight?\n")

if int(weight) < 0:
    print("Please enter a number larger than zero")
    weight = input("Please reenter your weight\n")

# planet_choice = input(
#     "Enter a planet name to find what your weight would be there\n")


def find_all_weights(x):
    for key, value in planets.items():
        # new_weight = float(value) * int(weight)
        new_weight = round(int(weight) * float(value), 2)
        print(f"{first_name}, your weight on {key} would be {new_weight} pounds")


print(find_all_weights(weight))


# def find_new_weight(x, y):
#     for key, value in planets.items():
#         if key == planet_choice:
#             # print(planet_choice)
#             # print(type(value))
#             new_weight = float(value) * int(weight)
#     return f"{first_name}, your weight on {planet_choice} would be {new_weight} pounds!"


# print(find_new_weight(planet_choice, weight))


# input must be converted to integer so to prevent multiplication from repeating versus computing
# function needed to take two arguments, since it will eventually take in user inputs
# looped through dictionary of planet names and gravity conversions, if planet name (key) matched user input, then multiply new weight based off the planet's gravity conversion value
# needed to make planet value a float in order to prevent some calculations rounding to 0
