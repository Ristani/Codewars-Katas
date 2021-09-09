def printer_error(s):
    goodletters = "abcdefghijklm"
    totalletters = len(s)
    errors = sum(letter not in goodletters for letter in s)
    return str(errors) + "/" + str(totalletters)
