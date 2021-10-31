# Bite 1 Sum N Numbers

"""
Write a function that can sum up numbers:

It should receive a sequence of n numbers.
If no argument is provided, return sum of numbers 1..100.
Look closely to the type of the function's default argument ...
Have fun!
"""

def sum_numbers(numbers=None):
    if numbers:
        return sum(numbers)
    elif isinstance(numbers, list):
        return 0
    else:
        return sum(range(101))