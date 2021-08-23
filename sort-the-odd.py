"""
odds = sorted((x for x in arr if x % 2 != 0), reverse = True)

generator = (x for x in arr if x % 2 != 0), This is a generator to get the odds in arr

odds = sorted(generator, reverse = True), sort the result of generator from big to small, store it in odds

return [x if x % 2 == 0 else odds.pop() for x in arr]

   This is a combination of list comprehension and conditional expression
   conditional expression part is ‘ x if x % 2 == 0 else odds.pop()
   list comprehension part is ‘x for x in arr’

 this statement equals to :
 for x in arr:
    if x % 2 == 0:
        return x
    else:
        return odds.pop()

 odds.pop() will delete the last item in list odds and give a return value of the deleted item
 >>>[1, 2, 3].pop()
   3
"""

def sort_array(arr):
    odds = sorted((x for x in arr if x%2 != 0), reverse=True)
    return [x if x%2==0 else odds.pop() for x in arr]