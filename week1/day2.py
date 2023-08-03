from enum import Enum

# ternary operator


def is_adult(age):
    return True if age > 18 else False


# Strings
#print("""My name is Rob""")

# Built in methods
# .upper .lower
# replace() replace part of a string
# split() split a string on a specific character separator
# join() to append new letters to a string
# find() fin the position of a substring
name = "mowglie"
# print("rob".upper())
#print("captain mowglie".title())
# print("ow" in name)  # True

print(name[-1])  # e


# numbers
# print(abs(-5.5))  # 5.5
# print(round(5.24, 1))  # 5.2


class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5


# print(list(Day))  # prints list
# print(len(Day))  # 5

#age = input("What is your age? ")
#print("Your age is " + age)


# Lists

dogs = ["Mowglie", "Marvin", "Rocky", "Goose"]
numList = [1, 5, 4, 8, 2, 10]

# print("Roger" in dogs)  # true
# print(dogs[2])  # Marvin

# print(dogs[2:4])  # Marvin, Rocky
# print(dogs.pop())  # Goose
# print(dogs[2:])  # rocky (Goose was removed with pop())

numListcopy = numList[:]
numList.sort()
# print(numList)  # (1,2,4,5,8,10)
# print(numListcopy)

# sorted function does not change original list

# sorted(numList, key=str.lower) # works better with str list
# print(numList)


# Tuples - create immuteable lists

name = ("Roger", "Champ")

name[-2]
name.index("Roger")

len(name)

print("Roger" in name)


# Dictionaries - key/value formatted list

dog = {"Name": "Roger", "age": 7, "color": "red"}
print(dog.get("Name"))  # Roger
print(dog['age'])  # 7
print("color" in dog)  # true
print(dog.values())  # Roger, 7, red
# puts all items of dictionary into list [(Name, Roger) (age, 7)]
print(dog.items())
print(len(dog))


# Sets - unordered, unique elements, no duplicates, can be modified, but the elements
# are immutable

set1 = {"Rob", "Kelly"}
set2 = {"Rob"}
set3 = {"Luna"}
mod = set1 - set2
mod1 = set1 | set2 | set3  # Kelly, Rob | Kelly, Rob, Luna

print(mod)  # Kelly


# Functions
def hello(name="friend "):
    print("Hello " + name)


hello("Rob")
hello("Mowglie")
hello()

# Variable Scope

age = 8  # Global variable


def test():
    print(age)

# local variable, only available inside the function


def test2():
    age = 10
    print(age)


def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)


#talk("I am going to have a beer tonight")


def counter():
    count = 0

    def increment():
        nonlocal count  # used to grab non-local variable from parent function
        count = count + 1
        return count

    return increment  # return the value of this function


increment = counter()  # reassign value of variable to parent function

print(increment())
print(increment())
