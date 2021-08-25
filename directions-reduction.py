def dirReduc(arr):
    # Stores a dictionary of directions and their opposites.
    dirs = {"NORTH":"SOUTH", "SOUTH":"NORTH", "WEST":"EAST", "EAST":"WEST"}
    # Creates an empty results list
    results = []
    # For each direction passed
    for i in arr:
        # If the current iterant is the opposite of the last stored result
        if results and dirs[i] == results[-1]:
            # Remove it
            results.pop()
        # Otherwise
        else:
            # Add it
            results.append(i)
    # Return the string of reduced directions
    return results