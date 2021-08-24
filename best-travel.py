"""
John and Mary want to travel between a few towns A, B, C ...
Mary has on a sheet of paper a list of distances between these towns.
ls = [50, 55, 57, 58, 60].
John is tired of driving and he says to Mary that he doesn't
want to drive more than t = 174 miles and he will visit only 3 towns.

Which distances, hence which towns, they will choose so that
the sum of the distances is the biggest possible - to please Mary -
but less than t - to please John- ?

t-max distance
k- number of towns
ls-list of distances
"""

import itertools

def choose_best_sum(t, k, ls):
    # For each combination, get a total value, sorted and reversed
    sums = sorted([sum(i) for i in itertools.combinations(ls, k)], reverse = True)
    # Loop through in descending order
    for i in sums:
        # Find the first possible value less than the limiter
        if i <= t:
            # Return it
            return i
    # If all possible combinations exceed the limit
    else:
        # Return none
        return None
