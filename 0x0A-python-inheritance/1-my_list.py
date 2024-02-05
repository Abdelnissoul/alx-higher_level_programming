#!/usr/bin/python3
"""Module of an inherited class MyList."""


class MyList(list):
    """class that will sort printing for list class."""

    def print_sorted(self):
        """Prints the list as sorted"""
        print(sorted(self))
