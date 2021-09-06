from itertools import groupby


def group_consecutive(lst):
    for _, g in groupby(enumerate(lst), lambda i_x: i_x[0] - i_x[1]):
        r = [x for _, x in g]
        if len(r) > 2:
            yield f"{r[0]}-{r[-1]}"
        else:
            yield from map(str, r)


def solution(lst):
    return ','.join(group_consecutive(lst))


"""
enumerate takes an iterable and returns a sequence of pairs where the first element is the index in the iterable, and
the second is the value

e.g. enumerate([1, 4, 5, 6, 9]) returns ((0,1), (1,4), (2,5), (3,6), (4,9)).

If a set of numbers belong to a sequence, their value minus their index should all be the same (assuming the numbers
are sorted). So using the previous example:
[i for i in map(lambda p: p[1]-p[0], enumerate([1,4,5,6,9]))] returns [1, 3, 3, 3, 5].

groupby combines all entries with the same key (in this case, the result of the lambda expression):
[[j for j in i[1]] for i in groupby(enumerate([1,4,5,6,9]), lambda p: p[1]-p[0])]
returns [[(0, 1)], [(1, 4), (2, 5), (3, 6)], [(4, 9)]]

Then it's simply a matter of building the output string:

If the sublist has 3 or more elements use "-" as the delimiter and the first and last element as the values
If the sublist has 2 elements use "," as the delimiter and the first and last element as the values
If the sublist has only 1 element, just use its value.
"""


def range_extraction(args):
    groups = ([v[1] for v in g] for _, g in groupby(enumerate(args), lambda p: p[1] - p[0]))
    return ','.join('{}{}{}'.format(g[0], '-' if len(g) > 2 else ',', g[-1])
                    if len(g) > 1 else str(g[0]) for g in groups)
