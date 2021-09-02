"""
Description:
You are going to be given a word. Your job is to return the middle
character of the word. If the word's length is odd, return the middle
character. If the word's length is even, return the middle 2 characters.

Examples:

    Kata.getMiddle("test") should return "es"
    Kata.getMiddle("testing") should return "t"
    Kata.getMiddle("middle") should return "dd"
    Kata.getMiddle("A") should return "A"
"""

def get_middle(s):
    # If the string length is even.
    if len(s) % 2 == 0:
        # Return the middle two characters.
        return s[len(s)//2-1] + s[len(s)//2]
    # Else its odd.
    else:
        # So we return just the middle.
        return s[len(s)//2]