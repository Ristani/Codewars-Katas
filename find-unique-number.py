"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

It’s guaranteed that array contains at least 3 numbers.
"""


def find_uniq(arr):
    # Sorts the given array.
    arr.sort()
    # Returns the first value if it's less than the last two, otherwise the last must be unique.
    return arr[0] if(arr[0] < arr[-1] and arr[0] < arr[-2]) else arr[-1]
