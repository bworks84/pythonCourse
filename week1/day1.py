name = "rob"
age = 39
age = int("39")
rob = {"name": "Rob", "age": age}
print(rob["age"])
print(isinstance(name, str))  # -> True
print(isinstance(age, int))  # -> True


# Arithmetic Operators

4 % 3  # 1 # modulo or remainder operator
4 ** 2  # 16 exponential
4 // 2  # 2 - Floor division, divides and rounds down to nearest whole number
# 42 - can use with any simple arithmetic operators to simplify equation (ex. *=, -=)
age += 3

a = 1
b = 2
a == b  # False - comparison operator (True/False)
a != b  # True - comparison does not equal operator (True/False)
a > b  # False - Greater than operator
a <=  # True - Less than or equal to


# Truthy/Falsey
print(0 or 1)  # 1
print(False or 'hey')  # hey
print('hi' or 'hey')  # hi because its first
# False because empty dict is a falsey value and first value read
print([] or False)
print(False or [])  # [] opposite of line above
