""" 
Rob Works
Python Essentials
8/23/23

Restaurant Bill:

Write a Python script that informs a user of their total meal charges. 

Prompt the user for the amount of the meal (e.g. $32.95).
Compute the tax on the restaurant bill. The tax should be 6.75 percent of the meal cost. 
Prompt the user for the tip amount (Suggesting a value equal to 18 percent of the total).
Display the meal cost, tax amount, tip amount, and total bill on the screen
"""

print("The cost for your meal is $32.95")
costOfMeal = 32.95
mealTax = .0675
mealPlusTax = []


def computeTax(num, mealTax):
    tax = round(num * mealTax, 2)
    totalCost = tax + num
    mealPlusTax.append(totalCost)
    return f"The amount of tax on your meal is ${tax}."

    # print(mealPlusTax)

# Goal: don't rewrite code from computeTax func. Add totalCost to global variable that holds value in list, then use that element from variable in next function to calculate tip. Return f string to make dynamic.


def computeTip(x):
    tip = round(mealPlusTax[0] * .18, 2)
    return f"We suggest a tip of 18 percent, which would be ${tip}. If you are so generous, that would bring the total to ${mealPlusTax[0] + tip}. "


print(computeTax(costOfMeal, mealTax))
print(computeTip(mealPlusTax))
