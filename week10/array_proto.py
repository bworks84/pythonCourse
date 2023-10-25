# Write code that enhances all arrays such that you can call the array.last() method on any array and it will return the last element. If there are no elements in the array, it should return -1.

# You may assume the array is the output of JSON.parse.

def array_pop(n):
    if n == []:
        return -1
    else:
        last_el = n.pop()
    return last_el


# print(array_pop([1, 2, 3, 4]))
print(array_pop([]))


# javascript
# NOTES: Array.prototype.last = function() {

# This line begins by extending the Array.prototype with a new method called last. This means that all JavaScript arrays will now have access to this method.
# return this.length > 0 ? this[this.length-1] : -1;

# This is the implementation of the last method. It checks if the length of the array (this.length) is greater than 0.

# If the array has elements (length is greater than 0), it returns the last element of the array using this[this.length-1]. The this keyword refers to the array itself, and this.length-1 retrieves the last element because array indices are zero-based.

# If the array is empty (length is 0), it returns -1. This is indicated by the : -1 part of the conditional (ternary) operator.

# };

# Array.prototype.last = function() {
#     return this.length > 0 ? this[this.length-1]: -1;


# };
