"""
You will be given a number and you will need to return it as a string in Expanded Form.

For example:
	expanded_form(12)    # Should return '10 + 2'
	expanded_form(42)    # Should return '40 + 2'
	expanded_form(70304) # Should return '70000 + 300 + 4'

NOTE: All numbers will be whole numbers greater than 0.
"""

def expanded_form(num):
	# Generate a blank list.
    list = []
    # Divide by tenths spacing.
    tenth = 10
    # While the number is divisible.
    while tenth < num:
    	# And doesn't 0 out.
        if num % tenth != 0:
        	# Insert the value into the results list.
            list.insert(0, str(num % tenth))
        # Subtract the divided amount from the number.
        num -= num % tenth
        # Increase the tenth to the next space, and repeat.
        tenth *= 10
    # If not divisible, insert the remaining value to the list.
    list.insert(0, str(num))
    # Return the joined string
    return ' + '.join(list)
