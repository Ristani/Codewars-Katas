"""
Given a positive integer n, calculate the following sum:

    n + n/2 + n/4 + n/8 + ...

All elements of the sum are the results of integer division.

Example:
    25  =>  25 + 12 + 6 + 3 + 1 = 47
"""

def halving_sum(n):
    result = 0
    while n >= 1:
        result += n
        n = (n * 1) // 2
    return result