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

cost_of_meal = float(input("Enter the cost of your meal\n"))
print(f"You entered ${cost_of_meal} as the cost of your meal")
mealTax = .0675
meal_plus_tax = []


def computeTax(cost_of_meal, mealTax):
    tax = round(cost_of_meal * mealTax, 2)
    meal_plus_tax_result = tax + cost_of_meal
    meal_plus_tax.append(meal_plus_tax_result)

    return f"The amount of tax on your meal is ${tax}, based on a {mealTax * 100}% sales tax"


# Goal: don't rewrite code from computeTax func. Add totalCost to global variable that holds value in list, then use that element from variable in next function to calculate tip. Return f string to make dynamic.


def computeTip(x):
    tip = round(meal_plus_tax[0] * .18, 2)
    return f"We suggest a tip of 18 percent, which would be a ${tip} tip. If you are so generous, that would bring the total to ${meal_plus_tax[0] + tip}. "


print(computeTax(cost_of_meal, mealTax))
print(computeTip(cost_of_meal))
