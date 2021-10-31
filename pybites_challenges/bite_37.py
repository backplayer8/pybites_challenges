# Bite 37: Rewrite a for loop using recursion

"""
Although you have to be careful using recursion it is
one of those concepts you want to at least understand.
It's also commonly used in coding interviews :)

In this beginner Bite we let you rewrite a simple countdown
for loop using recursion. See countdown_for below, it produces
the following output:

$ python countdown.py
10
9
8
7
6
5
4
3
2
1
time is up
You will be tested on having the same output,
making it work with another start value,
and of course if you used recursion. Have fun!
"""


def countdown_for(start: int = 10):
    for i in reversed(range(1, start + 1)):
        print(i)
    print("time is up")


def countdown_recursive(start: int = 10):
    if start < 0:  # Avoids recursion limit if given a negative start value
        start -= start + start
    """ This is a fake docstring to test pre-commit
        this is a pretty cool feature.
    """
    if start == 0:
        print("time is up")
    else:
        print(start)
        countdown_recursive(start - 1)
