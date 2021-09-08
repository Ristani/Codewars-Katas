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


def who_likes_it(names):
    # make a dictionary d of all the possible answers. Keys are the respective number
    # of people who liked it.

    # {} indicate placeholders. They do not need any numbers but are simply replaced/formatted
    # in the order the arguments in names are given to format
    # {others} can be replaced by its name; below the argument "others = n - 2"
    # is passed to str.format()

    # [min(4, length)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min is necessary as len(names) may be > 4

    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = n - 2

    n = len(names)
    return {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
    }[min(4, n)].format(*names[:3], others=n-2)
