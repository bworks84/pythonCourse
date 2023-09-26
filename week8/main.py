print("Python Calculator")
print("This program will add, subtract, multiply or divide two integers")
print("Enter expression in form \"x <op> y\", e.g. 73 * 88")
calcmessage = input("Expression: ") 

def GetNumber(parameter):
    try:
        return int(parameter)
    except ValueError:
        raise NotNumericError(parameter)

parameters = calcmessage.split()
#print("Parameters:", type(parameters))
class NotNumericError(Exception):
    def __init__(self, parameter):
        self.parameter = parameter
        super().__init__(f"Error: A non-integer value was detected, {parameter}")
try:
    value1 = GetNumber(parameters[0])
    operator = parameters[1]
    value2 = GetNumber(parameters[2])
except NotNumericError as e:
    print(e)
    print("The input was not numeric")
    exit()
if operator == "+":
    result = value1 + value2
elif operator == "-":
    result = value1 - value2
elif operator == "*":
    result = value1 * value2
elif operator == "/":
    result = value1 / value2
print(value1, " ", operator, " ", value2, " = ", result)



# Notes:
# run python <filename>, type in expression to check error handling

# Step 1 - try checking if converted parameters[0] and parameters[2] are integers
# Step 2 - if parameters fail, raise NotNumericError class with given default message from Exception parent class
# Step 3 - Build custom exception class, that takes in built-in Exception class, used to handle conditions where a non-int value is found from input. Define the constructor method __init__ that takes in the parameter in question (the non-int value), and call the constructor of the parent class (Exception) that prints an f string that identifies the error. 
# Step 4 - add 2nd string to match error message format