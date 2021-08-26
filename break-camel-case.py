"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
'camelCasing'  =>  'camel Casing'
'identifier'   =>  'identifier'
''             =>  ''
"""

def break_camel_case(s):
    # For characters in string if the letter is uppercase put a space before it.
    return ''.join(' ' + c if c.isupper() else c for c in s)