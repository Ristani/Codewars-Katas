"""
Write a function dirReduc which will take an array of strings and returns an
array of strings with the needless directions removed (W<->E or S<->N side by
side).

Notes
Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"]
is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST"
are not directly opposite of each other and can't become such. Hence the result
path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
"""

def dirReduc(arr):
    # Stores a dictionary of directions and their opposites.
    dict = {"NORTH":"SOUTH", "SOUTH":"NORTH", "WEST":"EAST", "EAST":"WEST"}
    # Creates an empty results list.
    list = []
    # For each direction passed.
    for i in arr:
        # If the current iterant is the opposite of the last stored result.
        if list and dict[i] == list[-1]:
            # Remove it.
            list.pop()
        # Otherwise.
        else:
            # Add it.
            list.append(i)
    # Return the string of reduced directions.
    return list