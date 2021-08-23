"""
Takes a string 'someKindOfString' and returns 'some Kind Of String'
"""

def break_camel_case(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)