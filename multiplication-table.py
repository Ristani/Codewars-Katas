"""
Your task, is to create NxN multiplication table, of size provided in parameter.

For example, when given size is 3:

1 2 3
2 4 6
3 6 9

For given example, the return value should be: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
"""

def multiplication_table(size):
    # Create an empty list to return.
    list = []
    # For each row.
    for r in range(1, size + 1):
        # Create an empty list.
        row = [r * c for c in range(1, size + 1)]
        # Then add each row to the results list.
        list.append(row)
    # Return the nested lists.
    return list