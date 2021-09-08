"""
likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
"""


def likes(names):
    result = ""

    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return str(names[0]) + " likes this"
    elif 1 < len(names) < 4:
        for name in range(len(names) - 1):
            result = result + names[name] + ", "
        result = result[:-2]
        return result + " and " + str(names[len(names) - 1]) + " like this"
    else:
        for name in range(2):
            result = result + names[name] + ", "
        result = result[:-2]
        return result + " and " + str(len(names)-2) + " others like this"
