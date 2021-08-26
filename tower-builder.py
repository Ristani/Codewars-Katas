"""
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

for example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]

and a tower of 6 floors looks like below

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]
"""

def tower_builder(n_floors):
    # Get an empty list to draw the tower in.
    list = []
    # For each layer of the tower.
    for i in range(n_floors):
        # Add decreasing amounts of spaces on either side of increasing *'s to the list.
        list.append(' ' * (n_floors - i - 1) + '*' * (i * 2 + 1) + ' ' * (n_floors - i - 1))
    # Return the built tower.
    return list