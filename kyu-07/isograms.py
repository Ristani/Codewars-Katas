def is_isogram(string):
    occurrences = []
    string = string.lower()
    for c in string:
        if c.isalpha() and c not in occurrences:
            occurrences.append(c)
        else:
            return False
    return True
