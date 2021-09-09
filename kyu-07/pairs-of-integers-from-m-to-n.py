from itertools import combinations_with_replacement


def generate_pairs(m, n):
    return list(combinations_with_replacement(range(m, n+1), 2))
