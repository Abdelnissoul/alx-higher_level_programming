#!/usr/bin/python3
"""Module to find the max integer in a list"""


def max_integer(list=[]):
    """Function to find the max integer in a list of integers
        and return it, unless it is empty: function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    x = 1
    while x < len(list):
        if list[x] > result:
            result = list[x]
        x += 1
    return result
