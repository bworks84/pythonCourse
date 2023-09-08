"""
Program name: bar_graph.py

Author: Rob Works
Course: Python Essentials
Date : 9/5/2023
Assignment: Module 3 - Lab - Plot Bars
Purpose: Take a list of integers and plot a bar graph that replaces the value of the integer with a string character

"""


# Function to plot bar graphs
def plotBars(data_list, plotsymbol):
    # use a for loop to print 40 blank lines
    # this "clears" out the console window
    print(40 * "\n")
    # for each value in the list:
    #   print "value" number of plotsymbols using string replication
    for x in data_list:
        print(x * plotsymbol)
    print()


# Main Program
# Build a list of numbers between 1 and 50
theList = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

plotBars(theList, "*")
print("The data is:", theList)
print()


def bubbleSort(sorted_list):
    for outer_index in range(len(sorted_list)):
        # call plotBars subroutine
        for inner_index in range(0, len(sorted_list) - outer_index - 1):
            if sorted_list[inner_index] > sorted_list[inner_index + 1]:
                temp = sorted_list[inner_index]
                sorted_list[inner_index] = sorted_list[inner_index+1]
                sorted_list[inner_index+1] = temp
    # call plotBars subroutine
    plotBars(sorted_list, "*")


# Main Program
# Build a list of numbers between 1 an 50
another_list = [20, 1, 28, 17, 12, 38, 7, 34, 41]
third_list = [48, 32, 16, 2, 8, 43, 27, 21, 37]
bubbleSort(another_list)

print("The data was:", another_list)

print()
