"""
Write a function that takes in a string of one or more words, and
returns the same string, but with all five or more letter words
reversed (like the name of this kata).

Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Examples:
    spinWords("Hey fellow warriors") => "Hey wollef sroirraw" 
    spinWords("This is a test") => "This is a test" 
    spinWords("This is another test") => "This is rehtona test"
"""


def spin_words(sentence):
    # Split the sentence into a list.
    sentence = sentence.split()
    # Create an empty list to return.
    result = []
    # For each item in the received list.
    for word in sentence:
        # If the word is longer than five characters.
        if len(word) >= 5:
            # Add it to the results list backwards.
            result.append(word[::-1])
        # If it's shorter than five characters.
        else:
            # Add it normally.
            result.append(word)
    # Join and return the altered string.
    return " ".join(result)
