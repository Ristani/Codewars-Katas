"""
You will be given a vector of strings. You must sort it alphabetically
(case-sensitive, and based on the ASCII values of the chars) and then
return the first value.

The returned value must be a string, and have "***" between each of
its letters.

You should not remove or add elements from/to the array.
"""

def two_sort(list):
    # Sort the list.
    list = sorted(list)
    # Return the first value with each character separated by stars.
    return "***".join(list[0])