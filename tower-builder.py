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
    # Return the built tower.
    return [
        ' ' * (n_floors - i - 1) + '*' * (i * 2 + 1) + ' ' * (n_floors - i - 1)
        for i in range(n_floors)
    ]
