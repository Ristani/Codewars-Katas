import collections


def duplicate_count(text):
    text = text.lower()
    return len(list(filter(lambda x: x[1] > 1, collections.Counter(text).items())))
