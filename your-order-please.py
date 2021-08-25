"""
Your task is to sort a given string. Each word in the string will contain
a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input
String will only contain valid consecutive numbers.
"""

def order(sentence):
    # Splits the sentence string into an array.
    arr = sentence.split()
    # Create an empty list. 
    lst = {}
    # For each word in the array.
    for word in arr:
        # Search the characters.
        for char in word:
            # For the hidden number, 1 will exist and is 9 or less.
            if char.isdigit() and int(char) <= 9:
                # Assign the word to its index position within the list.
                lst[char] = word
    # Return the sorted list as a string.
    return " ".join(lst[i] for i in sorted(lst))