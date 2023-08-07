from itertools import zip_longest

# List Compression

numbers = [1, 2, 3, 4, 5, 6]

numbers_power_2 = [n**2 for n in numbers]

# print(numbers_power_2)  # [1, 4, 9, 16, 25, 36]


# Same as
numbers_power_2 = []
for n in numbers:
    numbers_power_2.append(n**2)

numbers_power_2 = list(map(lambda n: n**2, numbers))


# Polymorphism - the ability to call methods or variables from different types of classes/data types
class Dog:
    def eat(self):
        print("Eating dog food")


# animal1 = Dog()

# animal1.eat()


# Loops

num = [2, 5, 10, 4, 45, 17, 36, 8, 25, 50]

# Ascending

# for i in sorted(num):
# print(i)

# Descending

# for i in sorted(num, reverse=True):
# print(i)


names = ["Rob", "Kelly", "Bob", "Ian", "Mowglie", "Zeus"]

# for i in sorted(names):
# print(i)  # Bob, Ian, Kelly ->


dict1 = {"a": 3, "f": 2, "z": 10, "e": 9, "h": 7}
# for i in sorted(dict1.items()):
# print(i)  # sorts alphabetically ("a", 3)("e", 9) ->

# for i in sorted(dict1.keys()):
# print(i)  # a e f h z


# for i in sorted(dict1.values()):
# print(i)  # 2 3 7 9 10


num1 = [1, 2, 3, 4]

# for i in reversed(num1):
# print(i) # 4 3 2, 1


employees = [{"name": "Rob", "age": 19}, {"name": "Kelly", "age": 15}, {"name": "Jim", "age": 18},
             {"name": "Gary", "age": 16}, {"name": "Sarah", "age": 21}, {"name": "Beau", "age": 17}]

# for employees in filter(lambda i: i["age"] % 2 == 0, employees):
# print(employees)  # {'name': 'Jim', 'age': 18} & prints Gary dict


country = ["USA", "UK", "India", "China",
           "Brazil", "France", "Germany", "Mexico"]

# while country:
# removes each country and prints name until country list is empty of elements
# print(country.pop(-1))

num = 10
# while num > 0:
# num -= 1
# print(num)  # 9 -> 0

# for i in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']):
# print(i)  # (0, 'a') (1, 'b')

# for key, value in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']):
# print(key, value)  # prints key, value (0 a) instead of tuple (line 88)

first = ['Rob', 'Kelly', 'Mowglie']
last = ['Works', 'Koriakin', 'Bear']
num = [1, 2, 3, 4, 5]
# for i in zip(first, last, num):
# print(i)  # ('Rob', 'Works', 1) ->


first = ['Rob', 'Kelly', 'Mowglie', 'Joe', 'Buck']
last = ['Works', 'Koriakin', 'Bear']
for i in zip_longest(first, last, fillvalue='Not Given'):
    print(i)
