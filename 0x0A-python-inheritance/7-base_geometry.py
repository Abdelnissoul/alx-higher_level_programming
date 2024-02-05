#!/usr/bin/python3
"""a base geometry class"""


class BaseGeometry:
    """defining the class base geometry."""

    def area(self):
        """shows the area without implementing it"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that Validates the parameter int.

        Args:
            name : the name of the parameter.
            value : the value of parameter.
        Raises:
            TypeError: If value isn't an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
