# Given an integer numRows, return the first numRows of Pascal's triangle.

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

def pascal_triangle(numRows):
    triangle = []

    for i in range(numRows):
        row = [1] * (i + 1)
        print("row = ", row)

        for j in range(1, i):
            print("j = ", j)
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            print("row[j] = ", row[j])

        triangle.append(row)

    return triangle


print(pascal_triangle(5))


# def generate_pascals_triangle(numRows):

# Defines a function called generate_pascals_triangle that takes an integer numRows as an argument.
# triangle = []

# Initializes an empty list named triangle to store the rows of Pascal's triangle.
# for i in range(numRows):

# Starts a loop that iterates from 0 to numRows - 1. This loop represents each row of Pascal's triangle.
# row = [1] * (i + 1)

# Creates a new list named row with i + 1 elements, all initialized to 1. This list represents the current row being constructed.
# for j in range(1, i):

# Starts another loop that iterates from 1 to i - 1. This loop calculates the values inside the current row, excluding the first and last elements which are always 1.
# row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

# Calculates the value at position j in the current row by summing the corresponding elements from the previous row (i - 1).
# triangle.append(row)

# Appends the completed row to the triangle list.
# return triangle

# Returns the completed Pascal's triangle as a list of lists
