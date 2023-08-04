import sys
from functools import reduce

# Objects - variables that contain data and functions that can be used to manipulate the data
# everything in python is treated as an object including vars, funcs, lists, tuples, dictionaries, set
items = [1, 2, 3, 4, 5]
items.append(6)
print(items)


# Loops

condition = True
# while condition == True:
# print("The condition is true")
# condition = False  # runs once

count = 0
# while count < 10:
# print("The condition is true")
# count += 1  # runs

print("After the loop")

# for item in items:  # items will print 6 lists with all elements
# print(item)  # item will print one list with each element on a sep line


# for item in range(10):
# print(item)

names = ["Rob", "Bobbie", "Arnie", "Kelly"]
# for index, name in enumerate(names):
# print(index, name)                 # prints index along with element


# for item in items:
# if item == 2:
# break
# print(item)  # only prints 1, then breaks the loop


# Classes

class Animal:
    def walk(self):
        print("Walking...")


class Dog(Animal):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")


mowglie = Dog("Mowglie", 10)

# print(type(mowglie))
# print(mowglie.name)
# print(mowglie.age)
# mowglie.bark()
# mowglie.walk()  # inherits function from parent class


# Module - every python file is a module

# Accepting Arguments

print(sys.argv)


# Lambda functions

lambda num: num * 2


def multiply(a, b): return a * b


print(multiply(2, 4))  # 8


# map, filter, reduce

items1 = [1, 2, 3, 4, 5, 6]


# def double(a):
# return a * 2

def double(a): return a * 2  # same as func above


# iterate through the second argument using the function called as the first argument
result = map(double, items1)

# print(list(result))  # [2, 4, 6]


def isEven(n):
    return n % 2 == 0


result = filter(isEven, items)
# print(list(result))  # 2, 4, 6


expenses = [
    ("Dinner", 80),
    ("Cell bill", 195),
]

sum = 0
# for expense in expenses:
# print("before: ", sum)
# expense[1] is each item at the 2nd element, expense[0] = string
# sum += expense[1]
# print("after: ", sum)

# print(sum)

sum = reduce(lambda a, b: a[1] + b[1], expenses)  # 275

# print(sum)

# Recursion - a function can call itself

# Factorial
# 3! = 3 * 2 * 1 = 6
# 4! = 4 * 3 * 2 * 1 = 24


def factorial(n):
    if n == 1:
        return 1  # base case, when we exit the function
    return n * factorial(n-1)  # if does not fit base case, do this


# print(factorial(3))
# print(factorial(4))

# Decorator - a design pattern that allows a user to add new functionality to an existing object without modifying its structure, typically called before the definition of a function you want to decorate

def logtime(func):
    def wrapper():          # acts as a decorator function
        print("before")
        val = func()
        print("after")
        return val
    return wrapper


@logtime                    # this is a decorator, applies logtime to hello()
def hello():
    print("hello")


hello()  # because of the @logtime decorator, the hello func is wrapped
# by the wrapper func defined inside logtime.
