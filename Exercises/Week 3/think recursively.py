# https://realpython.com/python-thinking-recursively/
"""
Appoint an elf and give all the work to him
Assign titles and responsibilities to the elves based on the number of houses for which they are responsible:
> 1 He is a manager and can appoint two elves and divide his work among them
= 1 He is a worker and has to deliver the presents to the house assigned to him



houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]


def deliver_presents_recursively(houses):

    # base case
    if len(houses) == 1:
        print("Delivering present to", houses[0])

    # recursive case
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)


deliver_presents_recursively(houses)


"""

"""
Calculate n! recursively



def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


print(factorial_recursive(5))"

"""


"""
Calculate the fibonacci sequence recursively

"""


from functools import lru_cache
@lru_cache(maxsize = None)
def fibonacci_recursive(n):

    # base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # recursive case
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
