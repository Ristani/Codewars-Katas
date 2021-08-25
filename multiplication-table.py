"""
Your task, is to create NxN multiplication table, of size provided in parameter.

For example, when given size is 3:

1 2 3
2 4 6
3 6 9

For given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
"""

def multiplication_table(size):
    # Create an empty table to return.
    result = []
    # For each row.
    for r in range(1, size+1):
        #Create an empty table.
        row = []
        # And with each column.
        for c in range(1, size+1):
            # Multiply and append the results.
            row.append(r * c)
        # Add each row as it's own table of results.
        result.append(row)
    # Return the whole table.
    return result