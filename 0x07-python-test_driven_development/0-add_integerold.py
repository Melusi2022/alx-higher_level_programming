#!/usr/bin/python3
"""

Module to add integers

"""


def add_integer(a, b=98):
    """
    Method to add integers
    """
    try:
        return int(a + b)
    except:
        if type(a) is not int and type(a) is not float:
            print("a must be an integer", end='')
            return
        elif type(b) is not int and typ(b) is not float:
            print("b must be an integer", end='')
            return
