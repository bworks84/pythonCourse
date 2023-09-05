import sys

calcmessage = input(
    "Please enter a simple calculation using two numbers and an arithmetic operator\n")
parameters = calcmessage.split()

val1 = float(parameters[0])
operator = parameters[1]
val2 = float(parameters[2])


# def compare_calc():
#     if operator == "+":
#         result = val1 + val2
#         return result
#     elif operator == "-":
#         result = val1 - val2
#         return result
#     elif operator == "*":
#         result = val1 * val2
#         return result
#     else:
#         result = val1 / val2
#         return result


# print(compare_calc())

##############################
# switch statement
# required installing python@3.10
# followed directions from freecodecamp listed in assignment
# print(sys.version)

match operator:
    case "+":
        result = val1 + val2
    case "-":
        result = val1 - val2
    case "*":
        result = val1 * val2
    case _:
        result = val1 / val2
