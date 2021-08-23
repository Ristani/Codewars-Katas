"""
Given a list of mostly identical values, sorts and compares the first with the last two to find the unique value
"""

def find_uniq(arr):
    arr.sort()    
    return arr[0] if(arr[0] < arr[-1] and arr[0] < arr[-2]) else arr[-1]