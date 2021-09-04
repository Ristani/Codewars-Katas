"""
Write a function dir_reduce which will take an array of strings and returns an
array of strings with the needless directions removed (W<->E or S<->N side by
side).

Notes
Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"]
is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST"
are not directly opposite of each other and can't become such. Hence the result
path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
"""


def dir_reduce(arr):
    # Stores a dictionary of directions and their opposites.
    rev_dir = {"NORTH": "SOUTH", "SOUTH": "NORTH", "WEST": "EAST", "EAST": "WEST"}
    # Creates an empty results list.
    result = []
    # For each direction passed.
    for i in arr:
        # If the current iterate is the opposite of the last stored result.
        if result and rev_dir[i] == result[-1]:
            # Remove it.
            result.pop()
        # Otherwise.
        else:
            # Add it.
            result.append(i)
    # Return the string of reduced directions.
    return result
