#!/usr/bin/python3
"""a class MyInt that inherits from int."""


class MyInt(int):
    """MyInt has == and != operators inverted"""

    def __eq__(self, op):
        """Override == with != behavior"""
        return self.real != op

    def __ne__(self, op):
        """Override != with == behavior."""
        return self.real == op
