"""
Given a list lst and a number N, create a new list that contains each
number of lst at most N times without reordering. For example if N = 2,
and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next
[1,2] since this would lead to 1 and 2 being in the result 3 times, and
then take 3, which leads to [1,2,3,1,2,3].

Example
  delete_nth ([1,1,1,1],2) # return [1,1]
  
  delete_nth ([20,37,20,21],1) # return [20,37,21]
"""

def delete_nth(order,max_e):
    # Get a new list that we will return.
    list = []
    # Get a dictionary to count the occurences.
    dict = {}
    # Loop through all provided numbers.
    for n in order:
        # Get the count of the current number, or assign it to 0.
        count = dict.setdefault(n, 0)
        # If we reached the max occurence for that number, skip it.
        if count >= max_e:
            continue
        # Add the current number to the list.
        list.append(n)
        # Increase the occurrences.
        dict[n] += 1
    # Return the list.
    return list