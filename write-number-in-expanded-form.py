"""
You will be given a number and you will need to return it as a string in Expanded Form.

For example:
	expanded_form(12)    # Should return '10 + 2'
	expanded_form(42)    # Should return '40 + 2'
	expanded_form(70304) # Should return '70000 + 300 + 4'

NOTE: All numbers will be whole numbers greater than 0.
"""

def expanded_form(num):
	# Generate a blank table
    result = []
    # Default divisible spacing
    divider = 10
    # If the (remaining) number is divisible
    while divider < num:
    	# And doesn't 0 out
        if num % divider != 0:
        	# Insert the value into the results table
            result.insert(0, str(num % divider))
        # Subtract the divided amount from the number
        num -= num % divider
        # Increase the divider to the next tenth space, and repeat
        divider *= 10
    # If not divisible, insert the remaining value to the results
    result.insert(0, str(num))
    # Return the joined string
    return ' + '.join(result)