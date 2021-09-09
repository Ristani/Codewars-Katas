"""
There is a queue for the self-checkout tills at the supermarket.
Your task is write a function to calculate the total time required
for all the customers to check out!

    Input
customers: An array of positive integers representing the queue.
           Each integer represents a customer, and its value is
           the amount of time they require to check out.

        n: a positive integer, the number of checkout tills.

    Output
The function should return an integer, the total time required.
"""


def queue_time(customers, n):
    time = [0] * n
    for i in customers:
        time[0] += i
        time.sort()
    return max(time)
